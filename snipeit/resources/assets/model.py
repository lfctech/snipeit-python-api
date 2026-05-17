"""Asset model."""

from __future__ import annotations

from typing import Any, ClassVar, Self

from pydantic import PrivateAttr

from ..base import ApiObject, _extract_payload

_MISSING = object()  # sentinel for "no value present"


class Asset(ApiObject):
    """Represents a Snipe-IT asset.

    Examples:
        Fetch and check out an asset:

            asset = api.assets.get(1)
            asset.checkout(checkout_to_type="user", assigned_to_id=123)
    """

    _resource_path: ClassVar[str] = "hardware"
    # Commonly-present fields declared for type checking convenience
    asset_tag: str | None = None
    name: str | None = None
    serial: str | None = None
    model: dict[str, Any] | None = None

    # Staged custom field values awaiting the next save(). Maps display label
    # (e.g. "Owner") to the new value. The label → column-name translation
    # (``_snipeit_<slug>_<id>``) happens at save() time using the live
    # ``custom_fields`` response shape.
    #
    # This is a dedicated channel — separate from the regular dirty tracker —
    # because Snipe-IT's custom field PATCH semantics are different from
    # regular fields: the wire format uses column names, the GET response
    # uses labels, and PATCH responses return ``custom_fields: null``.
    # Keeping staging out of ``_dirty_set()`` lets the base ``ApiObject``
    # remain agnostic about Snipe-IT's wire-format quirks.
    _pending_custom_fields: dict[str, Any] = PrivateAttr(default_factory=dict)

    def __repr__(self) -> str:
        asset_tag = self.asset_tag or "N/A"
        name = self.name or "N/A"
        serial = self.serial or "N/A"
        model = self.model
        model_name = model.get("name", "N/A") if isinstance(model, dict) else "N/A"
        return f"<Asset {asset_tag} ({name} - {serial} - {model_name})>"

    def checkout(self, checkout_to_type: str, assigned_to_id: int, **kwargs: Any) -> "Asset":
        """Check out this asset to a user, asset, or location.

        Args:
            checkout_to_type (str): One of "user", "asset", or "location".
            assigned_to_id (int): The id of the user/asset/location to assign.
            **kwargs: Additional optional fields such as expected_checkin, note, etc.

        Returns:
            Asset: The updated Asset object.

        Raises:
            ValueError: If checkout_to_type is not one of "user", "asset", or "location".
        """
        path = f"{self._path}/{self.id}/checkout"
        data: dict[str, Any] = {"checkout_to_type": checkout_to_type}
        if checkout_to_type == "user":
            data["assigned_user"] = assigned_to_id
        elif checkout_to_type == "asset":
            data["assigned_asset"] = assigned_to_id
        elif checkout_to_type == "location":
            data["assigned_location"] = assigned_to_id
        else:
            raise ValueError("checkout_to_type must be one of 'user', 'asset', or 'location'")
        data.update(kwargs)
        self._manager._create(path, data)
        return self.refresh()

    def checkin(self, **kwargs: Any) -> "Asset":
        """Check in this asset."""
        self._manager._create(f"{self._path}/{self.id}/checkin", kwargs)
        return self.refresh()

    def audit(self, **kwargs: Any) -> "Asset":
        """Audit this asset via POST /hardware/{id}/audit."""
        self._manager._create(f"{self._path}/{self.id}/audit", kwargs)
        return self.refresh()

    def restore(self) -> "Asset":
        """Restore a soft-deleted asset."""
        self._manager._create(f"{self._path}/{self.id}/restore", {})
        return self.refresh()

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def save(self) -> "Asset":
        """Persist regular dirty fields **and** any staged custom fields.

        Extends :meth:`ApiObject.save` to also flush ``_pending_custom_fields``.
        Each staged label is translated to its underlying column name
        (``_snipeit_<slug>_<id>``) using the asset's ``custom_fields``
        response shape, then merged into the PATCH body as a top-level key —
        the only format Snipe-IT's PATCH endpoint accepts for custom fields.

        If no regular fields are dirty *and* no custom fields are staged,
        no request is issued (matches base ``save()`` semantics).
        """
        dirty = self._dirty_set()
        data: dict[str, Any] = {f: getattr(self, f) for f in dirty}

        if self._pending_custom_fields:
            cfs = getattr(self, "custom_fields", None)
            if not isinstance(cfs, dict):
                # Defensive: a label was staged but the read shape is gone.
                # In normal flow this can't happen — set_custom_field validates
                # the label against custom_fields before staging — but if
                # custom_fields was wiped between staging and save (e.g. by a
                # manual setattr), surface a clear error rather than silently
                # dropping the change.
                raise RuntimeError(
                    "Cannot save staged custom fields: 'custom_fields' is not "
                    "available on this asset. Call refresh() and re-stage."
                )
            for label, value in self._pending_custom_fields.items():
                entry = cfs.get(label)
                if not isinstance(entry, dict) or "field" not in entry:
                    raise RuntimeError(
                        f"Cannot resolve column name for staged custom field "
                        f"{label!r}: 'custom_fields[{label!r}]' is missing or "
                        "malformed. Call refresh() and re-stage."
                    )
                data[entry["field"]] = value

        if not data:
            return self

        path = f"{self._path}/{self.id}"
        response = self._manager._patch(path, data)
        payload = _extract_payload(response)
        self._apply_server_data(payload)
        return self

    def _apply_server_data(self, data: dict[str, Any]) -> None:
        """Apply API data, accommodating Snipe-IT's PATCH response quirks.

        Snipe-IT's PATCH response payload has two oddities:

        1. ``custom_fields`` is always ``null`` in the response (the nested
           label-keyed read shape is not echoed back).
        2. The updated values are echoed at the **top level** as
           ``_snipeit_<col>`` keys instead. Stray column-name keys for
           fieldsets the asset does not even use also leak in.

        If we delegated this payload directly to ``ApiObject._apply_server_data``,
        the local ``custom_fields`` nested dict would be clobbered with
        ``None`` after every save, breaking ``set_custom_field`` on
        subsequent calls until ``refresh()``.

        This override:

        * Preserves the local ``custom_fields`` nested shape when the
          incoming payload's ``custom_fields`` is ``None`` and the local
          shape is a populated dict; refreshes each entry's ``["value"]``
          from the matching top-level ``_snipeit_*`` key in the payload.
        * Strips all ``_snipeit_*`` keys from the payload so they don't
          pollute ``__pydantic_extra__``.
        * Clears ``_pending_custom_fields`` after the server has acknowledged
          the changes.

        For GET responses (used by ``refresh()``), ``custom_fields`` arrives
        in the nested shape; the option-A branch below is skipped and the
        payload flows through unmodified.
        """
        incoming = dict(data)  # avoid mutating caller's dict

        existing_cfs = getattr(self, "custom_fields", None)
        incoming_cfs = incoming.get("custom_fields")
        if incoming_cfs is None and isinstance(existing_cfs, dict) and existing_cfs:
            refreshed: dict[str, Any] = {}
            for label, entry in existing_cfs.items():
                if not isinstance(entry, dict):
                    refreshed[label] = entry
                    continue
                new_entry = dict(entry)
                column = entry.get("field")
                if isinstance(column, str) and column in incoming:
                    new_entry["value"] = incoming[column]
                refreshed[label] = new_entry
            incoming["custom_fields"] = refreshed

        # Strip stray column-name keys. They've either been folded into the
        # nested shape above, or they belong to fieldsets this asset doesn't
        # use (Snipe-IT echoes them all). Either way they should not litter
        # __pydantic_extra__.
        incoming = {k: v for k, v in incoming.items() if not k.startswith("_snipeit_")}

        super()._apply_server_data(incoming)
        self._pending_custom_fields.clear()

    # ------------------------------------------------------------------
    # Custom fields
    # ------------------------------------------------------------------
    def pending_custom_fields(self) -> dict[str, Any]:
        """Return a copy of custom field values staged for the next ``save()``.

        Keys are display labels (e.g. ``"Owner"``); values are the new values
        passed to :meth:`set_custom_field`. The returned dict is a copy —
        mutating it does not affect staging state.

        Returns:
            dict[str, Any]: ``{label: value, ...}`` for every label that has
            been staged but not yet saved. Empty dict when nothing is staged.

        Example:
            >>> asset = api.assets.get(1)
            >>> asset.set_custom_field("Owner", "alice")
            >>> asset.pending_custom_fields()
            {'Owner': 'alice'}
            >>> asset.save()
            >>> asset.pending_custom_fields()
            {}
        """
        return dict(self._pending_custom_fields)

    def get_custom_field(self, label: str, default: Any = None) -> Any:
        """Return the value of a custom field by its display label.

        Reads ``custom_fields[label]["value"]`` from the asset's response shape.

        Args:
            label: The human-readable label of the custom field
                (e.g. ``"Owner"``), as it appears in the Snipe-IT UI and in
                the ``custom_fields`` response dict.
            default: Value returned when the field is not present on this
                asset. Defaults to ``None``.

        Returns:
            The current value of the custom field, or ``default`` if the
            field is not defined for this asset's model.

        Example:
            >>> asset = api.assets.get(1)
            >>> asset.get_custom_field("Owner")
            'alice'
        """
        cfs = getattr(self, "custom_fields", None)
        if not isinstance(cfs, dict):
            return default
        entry = cfs.get(label)
        if not isinstance(entry, dict):
            return default
        return entry.get("value", default)

    def set_custom_field(self, label: str, value: Any) -> Self:
        """Stage a custom field value for the next ``save()``.

        The staged value lives in :attr:`_pending_custom_fields` (inspectable
        via :meth:`pending_custom_fields`) until the next ``save()``, at which
        point ``Asset.save`` translates the label to its underlying column
        name (``_snipeit_<slug>_<id>``) via ``custom_fields[label]["field"]``
        and sends it as a top-level key in the PATCH body — the only format
        Snipe-IT's PATCH endpoint accepts for custom field updates.

        Cancellation: if ``value`` equals the field's current server value
        (read from ``custom_fields[label]["value"]``), any previous stage
        for this label is discarded and no PATCH is queued. This matches the
        no-op behaviour of plain attribute assignment on declared fields.

        Read semantics: the staged value does **not** update
        ``custom_fields[label]["value"]``; reads via :meth:`get_custom_field`
        continue to return the server's last-known value until ``save()``.
        Use :meth:`pending_custom_fields` to inspect what's staged.

        Args:
            label: The human-readable label of the custom field, as it
                appears in ``asset.custom_fields``. The asset must have been
                fetched (so ``custom_fields`` is populated) before calling
                this method.
            value: The new value to send to the server.

        Returns:
            self, to allow chaining (``asset.set_custom_field(...).save()``).

        Raises:
            KeyError: If ``label`` is not present in ``custom_fields``. This
                usually means either the asset has not been fetched yet, or
                the custom field is not associated with this asset's model.

        Example:
            >>> asset = api.assets.get(1)
            >>> asset.set_custom_field("Owner", "alice")
            >>> asset.save()
        """
        cfs = getattr(self, "custom_fields", None)
        if not isinstance(cfs, dict) or label not in cfs:
            raise KeyError(
                f"Custom field {label!r} is not defined on this asset. "
                f"Available labels: {sorted(cfs.keys()) if isinstance(cfs, dict) else []}. "
                "Make sure the asset has been fetched (api.assets.get) and that "
                "the field is associated with the asset's model fieldset."
            )
        entry = cfs[label]
        if not isinstance(entry, dict) or "field" not in entry:
            raise KeyError(
                f"Custom field {label!r} has unexpected shape: {entry!r}. "
                "Expected {'field': '_snipeit_...', 'value': ...}."
            )

        current = entry.get("value", _MISSING)
        if current == value:
            # Setting back to the server's current value cancels any pending
            # stage for this label. No PATCH will be queued.
            self._pending_custom_fields.pop(label, None)
            return self

        self._pending_custom_fields[label] = value
        return self
