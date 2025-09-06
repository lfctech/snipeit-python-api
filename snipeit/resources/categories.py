from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Category(ApiObject):
    """Represents a Snipe-IT category."""
    _path = "categories"

    def __repr__(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"


class CategoriesManager(Manager):
    """Manager for all Category-related API operations."""

    def list(self, **kwargs: Any) -> List['Category']:
        """
        Gets a list of categories.

        Args:
            **kwargs: Optional search parameters.

        Returns:
            A list of Categories.
        """
        return [Category(self, c) for c in self._get("categories", **kwargs)["rows"]]

    def get(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Gets a single category by its ID.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object.
        """
        return Category(self, self._get(f"categories/{category_id}", **kwargs))

    def create(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Creates a new category.

        Args:
            name: The name of the category.
            category_type: The type of category (asset, accessory, consumable, component, license).
            **kwargs: Additional optional fields.

        Returns:
            The newly created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        response = self._create("categories", data)
        return Category(self, response["payload"])

    def update(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: Additional optional fields.

        Returns:
            The updated Category object.
        """
        response = self._update(f"categories/{category_id}", kwargs)
        return Category(self, response["payload"])

    def patch(self, category_id: int, **kwargs: Any) -> 'Category':
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The updated Category object.
        """
        response = self._patch(f"categories/{category_id}", kwargs)
        return Category(self, response["payload"])

    def delete(self, category_id: int) -> None:
        """
        Deletes a category.

        Args:
            category_id: The ID of the category to delete.
        """
        self._delete(f"categories/{category_id}")
