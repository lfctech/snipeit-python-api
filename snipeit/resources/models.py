from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager
from ..exceptions import SnipeITApiError


class Model(ApiObject):
    """Represents a Snipe-IT asset model."""
    _path = "models"

    def __repr__(self) -> str:
        return f"<Model {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} ({getattr(self, 'model_number', 'N/A')})>"


class ModelsManager(Manager):
    """Manager for all Asset Model-related API operations."""

    def list(self, **kwargs: Any) -> List['Model']:
        """
        Gets a list of asset models.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Models.
        """
        return [Model(self, m) for m in self._get("models", **kwargs)["rows"]]

    def get(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Gets a single asset model by its ID.

        Args:
            model_id: If provided, retrieves a single model by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Model object.
        """
        return Model(self, self._get(f"models/{model_id}", **kwargs))

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
        response = self._create("models", data)
        return Model(self, response["payload"])

    def update(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Updates an existing asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Model object.
        """
        response = self._update(f"models/{model_id}", kwargs)
        return Model(self, response["payload"])

    def patch(self, model_id: int, **kwargs: Any) -> 'Model':
        """
        Partially updates an asset model.

        Args:
            model_id: The ID of the model to update.
            **kwargs: The fields to update.

        Returns:
            The updated Model object.
        """
        response = self._patch(f"models/{model_id}", kwargs)
        return Model(self, response["payload"])

    def delete(self, model_id: int) -> None:
        """
        Deletes an asset model.

        Args:
            model_id: The ID of the model to delete.
        """
        self._delete(f"models/{model_id}")
