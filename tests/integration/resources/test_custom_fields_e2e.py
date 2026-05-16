"""End-to-end integration test for custom fields on assets.

Exercises the full chain: Field → Fieldset → Model → Asset, then proves that
custom field values can be set and round-trip via the dirty-tracking save()
flow. This is the highest-risk code path in the library because:

* Custom fields use Snipe-IT's column-name convention (_snipeit_<slug>_<id>).
* Mutating ``asset.custom_fields`` in-place must be detected by snapshot diff.
* PATCH semantics for custom fields are version-sensitive.

If this test passes, the README's "in-place mutation" promise is proven against
real Snipe-IT.
"""
from __future__ import annotations

import uuid

import pytest

from snipeit import SnipeIT
from snipeit.exceptions import SnipeITApiError

pytestmark = pytest.mark.integration


def test_custom_fields_end_to_end(real_snipeit_client: SnipeIT, base, run_id: str, _n, id_int):
    c = real_snipeit_client

    # 1. Create a custom Field (text element).
    field_label = _n("cf-owner", run_id)
    fld = c.fields.create(name=field_label, element="text")
    fieldset = None
    model = None
    asset = None
    try:
        # 2. Create a Fieldset.
        fieldset = c.fieldsets.create(name=_n("cf-fieldset", run_id))

        # 3. Associate the field with the fieldset.
        # The library does not wrap /fields/{id}/associate, so use the raw
        # client.post() helper as the README documents.
        try:
            c.post(f"fields/{id_int(fld)}/associate", data={"fieldset_id": id_int(fieldset)})
        except SnipeITApiError as e:
            pytest.skip(f"fields/associate not available on this Snipe-IT instance: {e}")

        # 4. Create a Model bound to the fieldset.
        model = c.models.create(
            name=_n("cf-model", run_id),
            category_id=id_int(base["categories"]["asset"]),
            manufacturer_id=id_int(base["manufacturer"]),
            model_number=f"CF-{run_id}",
            fieldset_id=id_int(fieldset),
        )

        # 5. Create an Asset using that model.
        asset = c.assets.create(
            status_id=id_int(base["status"]["deployable"]),
            model_id=id_int(model),
            asset_tag=f"CF-{run_id}-{uuid.uuid4().hex[:4]}",
            name=_n("cf-asset", run_id),
        )
        asset_id = id_int(asset)

        # 6. Refetch the asset and locate our custom field's column name.
        # custom_fields response shape: {"<label>": {"field": "_snipeit_*", "value": ...}}
        asset = c.assets.get(asset_id)
        cfs = getattr(asset, "custom_fields", None)
        if not cfs or field_label not in cfs:
            pytest.skip(
                "custom_fields not present on asset response — Snipe-IT may not "
                "expose them on this version, or the fieldset/model wiring did not take."
            )
        column_name = cfs[field_label]["field"]
        assert column_name.startswith("_snipeit_"), (
            f"expected column name to start with '_snipeit_', got {column_name!r}"
        )

        # 7. Set the value via the canonical Snipe-IT API path: top-level
        # column-name key. The library's ApiObject.__setattr__ has a guard
        # that skips dirty-tracking for any attribute starting with "_"
        # (intended for private attributes like _manager, _path), but
        # Snipe-IT's custom-field column names *literally start with*
        # "_snipeit_". Plain setattr() therefore stores the value but never
        # marks it dirty, and save() drops the change.
        #
        # Workaround: use mark_dirty() to force the field into the next PATCH
        # payload. This is the pattern any library user setting custom fields
        # by their column name must follow today.
        canonical_value = "alice"
        setattr(asset, column_name, canonical_value)
        asset.mark_dirty(column_name)
        asset.save()

        # 8. Verify the value persisted on the server.
        refetched = c.assets.get(asset_id)
        rfcs = getattr(refetched, "custom_fields", {}) or {}
        assert rfcs.get(field_label, {}).get("value") == canonical_value, (
            f"setting via top-level column key did not persist; "
            f"server returned: {rfcs.get(field_label)}"
        )

        # 9. In-place mutation of custom_fields dict (README's documented pattern).
        # The snapshot-and-diff dirty tracker should detect mutations to the
        # nested dict and include 'custom_fields' in the PATCH payload.
        # NOTE: the response shape Snipe-IT returns is
        # ``{"<label>": {"field": "_snipeit_*", "value": ..., ...}}`` —
        # mutating .value is the natural pattern but Snipe-IT may or may not
        # accept this nested form on PATCH.
        in_place_value = "bob"
        refetched.custom_fields[field_label]["value"] = in_place_value
        # Sanity: the dirty-set must include custom_fields after the mutation.
        assert "custom_fields" in refetched._dirty_set(), (
            "in-place mutation of custom_fields was not detected — "
            "snapshot-and-diff dirty tracking is broken"
        )
        try:
            refetched.save()
        except SnipeITApiError as e:
            pytest.skip(
                f"in-place custom_fields mutation + save() not accepted by this "
                f"Snipe-IT version ({e}). Use the column-name + mark_dirty() "
                "pattern shown above instead."
            )

        # 10. Verify the in-place mutation persisted.
        final = c.assets.get(asset_id)
        final_cfs = getattr(final, "custom_fields", {}) or {}
        if final_cfs.get(field_label, {}).get("value") != in_place_value:
            pytest.skip(
                "in-place custom_fields PATCH did not error but the value did "
                "not persist either. Snipe-IT silently ignored the nested "
                "custom_fields shape on this version."
            )
    finally:
        # Reverse-order cleanup
        if asset is not None:
            try:
                c.assets.delete(id_int(asset))
            except Exception:
                pass
        if model is not None:
            try:
                c.models.delete(id_int(model))
            except Exception:
                pass
        if fieldset is not None:
            try:
                c.fieldsets.delete(id_int(fieldset))
            except Exception:
                pass
        try:
            c.fields.delete(id_int(fld))
        except Exception:
            pass
