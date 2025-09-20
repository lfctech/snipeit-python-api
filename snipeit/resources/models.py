"""Models resources.

Provides Model (asset model) and ModelsManager for Snipe-IT models.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Model(ApiObject):
    """Represents a Snipe-IT asset model.

    Examples:
        Fetch a model:

            mdl = api.models.get(1)
            print(mdl)
    """
    _path = "models"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The model id, name, and model number.
        """
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"


class ModelsManager(BaseResourceManager[Model]):
    """Manager for Asset Model-related API operations.

    Examples:
        Create a model:

            api.models.create(name="Latitude 5440", category_id=1, manufacturer_id=2)
    """

    resource_cls = Model
    path = Model._path

    def create(self, name: str, category_id: int, manufacturer_id: int, **kwargs: Any) -> 'Model':
        """Create a new asset model.

        Args:
            name (str): The name of the model.
            category_id (int): The category id this model belongs to.
            manufacturer_id (int): The manufacturer id for this model.
            **kwargs: Additional optional fields.

        Returns:
            Model: The newly created Model object.
        """
        data = {"name": name, "category_id": category_id, "manufacturer_id": manufacturer_id}
        data.update(kwargs)
        return super().create(**data)
