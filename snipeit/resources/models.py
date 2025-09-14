from typing import Any
from .base import ApiObject, BaseResourceManager


class Model(ApiObject):
    """Represents a Snipe-IT asset model."""
    _path = "models"

    def __repr__(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"


class ModelsManager(BaseResourceManager[Model]):
    """Manager for all Asset Model-related API operations."""

    resource_cls = Model
    path = Model._path

    def create(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """
        Creates a new asset model.

        Args:
            name: The name of the model.
            category_id: The ID of the category this model belongs to.
            manufacturer_id: The ID of the manufacturer of this model.
            **kwargs: Additional optional fields.

        Returns:
            The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        return super().create(**data)
