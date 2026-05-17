"""Asset model."""

from __future__ import annotations

from typing import Any, ClassVar, Self

from ..base import ApiObject

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
    # Custom fields
    # ------------------------------------------------------------------
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

        Looks up the underlying Snipe-IT column name (``_snipeit_<slug>_<id>``)
        from ``custom_fields[label]["field"]`` and arranges for it to be
        included in the next PATCH payload as a top-level key — the only
        format Snipe-IT's PATCH endpoint accepts for custom field updates.

        The value is also reflected back into ``custom_fields[label]["value"]``
        so subsequent reads via :meth:`get_custom_field` see the staged value
        without requiring a ``refresh()``.

        If the supplied ``value`` already matches the field's current value
        and the column is not already pending, this method is a no-op (no
        PATCH will be issued for this field on the next ``save()``). This
        mirrors the behaviour of plain attribute assignment on declared
        fields.

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
        column_name = entry["field"]

        # No-op skip: if the value is unchanged and the column isn't already
        # pending, do nothing — matches the no-op behaviour of plain
        # attribute assignment for declared fields (see ApiObject.__setattr__).
        current = entry.get("value", _MISSING)
        if current == value and column_name not in self._extra_dirty:
            return self

        # Stage the column-name field directly in __pydantic_extra__.
        #
        # Why not setattr()? Because Snipe-IT's column names start with '_',
        # pydantic v2's BaseModel.__setattr__ routes them into the instance
        # __dict__ rather than __pydantic_extra__. That works for getattr,
        # but the value would then linger in __dict__ across save()/refresh()
        # cycles (the base _apply_server_data only clears __pydantic_extra__,
        # not arbitrary __dict__ entries). Writing to __pydantic_extra__
        # directly keeps the staged value in the same bucket the lifecycle
        # code already manages, so it gets cleared automatically on save.
        extra = self.__pydantic_extra__
        if extra is None:
            extra = {}
            object.__setattr__(self, "__pydantic_extra__", extra)
        extra[column_name] = value
        self.mark_dirty(column_name)

        # Mirror the value into the nested response shape so reads see the
        # staged value before save()/refresh().
        entry["value"] = value
        # Also update the loaded-state snapshot so this mirror does not
        # cause snapshot-diff to mark `custom_fields` dirty and trigger an
        # unnecessary nested-shape PATCH (which Snipe-IT silently ignores
        # anyway). The column-name field is the only thing that should be
        # sent to the server.
        if isinstance(self._loaded_state, dict):
            snap_cfs = self._loaded_state.get("custom_fields")
            if isinstance(snap_cfs, dict) and isinstance(snap_cfs.get(label), dict):
                snap_cfs[label]["value"] = value
        return self
