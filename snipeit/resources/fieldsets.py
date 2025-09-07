from typing import Any, Dict, List
from .base import ApiObject, BaseResourceManager


class Fieldset(ApiObject):
    """Represents a Snipe-IT fieldset."""
    _path = "fieldsets"

    def __repr__(self) -> str:
        return f"<Fieldset {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')}>"


class FieldsetsManager(BaseResourceManager[Fieldset]):
    """Manager for all Fieldset-related API operations."""

    resource_cls = Fieldset
    path = Fieldset._path

    def create(self, name: str, **kwargs: Any) -> 'Fieldset':
        data = {"name": name}
        data.update(kwargs)
        return super().create(**data)
