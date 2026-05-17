"""End-to-end integration test for custom fields on assets.

Exercises the full chain: Field → Fieldset → Model → Asset, then proves that
custom field values can be set and round-trip via the dedicated
``set_custom_field`` / ``pending_custom_fields`` / ``save()`` flow.

This is the highest-risk code path in the library because:

* Custom fields use Snipe-IT's column-name convention (_snipeit_<slug>_<id>).
* PATCH responses return ``custom_fields: null`` and echo column-name keys
  at the top level — Asset._apply_server_data must fold them back so a
  second set_custom_field on the same in-memory instance still works.
* PATCH semantics for custom fields are version-sensitive.

If this test passes, the README's "stage and save repeatedly without
refresh()" promise is proven against real Snipe-IT.
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

        # 6. Refetch the asset and confirm the custom field shows up under its
        # display label.
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

        # 7. Stage and save via the canonical helper.
        first_value = "alice"
        result = asset.set_custom_field(field_label, first_value)
        # Returns self for chaining.
        assert result is asset
        # Staged in the dedicated channel.
        assert asset.pending_custom_fields() == {field_label: first_value}
        # Reads still see the server's current (empty/None) value.
        assert asset.get_custom_field(field_label) != first_value
        asset.save()
        # After save: pending cleared, get_custom_field reflects the new value
        # via the local nested-shape preservation in Asset._apply_server_data.
        assert asset.pending_custom_fields() == {}
        assert asset.get_custom_field(field_label) == first_value

        # 8. Verify on the server (independent fetch).
        refetched = c.assets.get(asset_id)
        assert refetched.get_custom_field(field_label) == first_value

        # 9. Two-cycle regression: a SECOND set_custom_field + save() on the
        # SAME in-memory asset (no refresh between) must persist correctly.
        # This is the main behaviour the refactor unlocked — Snipe-IT's PATCH
        # response sets custom_fields=null, and prior to the refactor that
        # would clobber the local nested shape and make this second call
        # raise KeyError.
        second_value = "bob"
        asset.set_custom_field(field_label, second_value).save()
        assert asset.get_custom_field(field_label) == second_value

        # 10. Verify the second value persisted on the server.
        final = c.assets.get(asset_id)
        assert final.get_custom_field(field_label) == second_value

        # 11. Cancellation: setting back to the server's value cancels the stage.
        asset.set_custom_field(field_label, "ghost")
        assert asset.pending_custom_fields() == {field_label: "ghost"}
        asset.set_custom_field(field_label, second_value)  # back to server
        assert asset.pending_custom_fields() == {}
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
