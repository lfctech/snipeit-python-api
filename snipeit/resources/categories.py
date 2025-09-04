from typing import Any, Dict, List, Optional, Union
from .base import ApiObject, Manager


class Category(ApiObject):
    """Represents a Snipe-IT category."""
    _path = "categories"

    def __repr__(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"


class CategoriesManager(Manager):
    """Manager for all Category-related API operations."""

    def get(self, category_id: Optional[int] = None, **kwargs: Any) -> Union['Category', List['Category']]:
        """
        Gets one or more categories.

        Args:
            category_id: If provided, retrieves a single category by its ID.
            **kwargs: Optional search parameters.

        Returns:
            A single Category object or a list of Categories.
        """
        if category_id:
            return Category(self, self._get(f"categories/{category_id}", **kwargs))
        else:
            return [Category(self, c) for c in self._get("categories", **kwargs)["rows"]]

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
        if response.get("status") == "success":
            return Category(self, response["payload"])
        return response

    def update(self, category_id: int, name: str, category_type: str, **kwargs: Any) -> Dict[str, Any]:
        """
        Updates an existing category.

        Args:
            category_id: The ID of the category to update.
            name: The new name of the category.
            category_type: The new type of the category.
            **kwargs: Additional optional fields.

        Returns:
            The API response dictionary.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        return self._update(f"categories/{category_id}", data)

    def patch(self, category_id: int, **kwargs: Any) -> Dict[str, Any]:
        """
        Partially updates a category.

        Args:
            category_id: The ID of the category to update.
            **kwargs: The fields to update.

        Returns:
            The API response dictionary.
        """
        return self._patch(f"categories/{category_id}", kwargs)

    def delete(self, category_id: int) -> None:
        """
        Deletes a category.

        Args:
            category_id: The ID of the category to delete.
        """
        return self._delete(f"categories/{category_id}")
