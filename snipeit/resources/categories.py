from typing import Any
from .base import ApiObject, BaseResourceManager


class Category(ApiObject):
    """Represents a Snipe-IT category."""
    _path = "categories"

    def __repr__(self) -> str:
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"


class CategoriesManager(BaseResourceManager[Category]):
    """Manager for all Category-related API operations."""

    resource_cls = Category
    path = Category._path

    def create(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """
        Create a new category.

        Args:
            name (str): The name of the category.
            category_type (str): The type of the category.
            **kwargs: Additional fields for the category.

        Returns:
            Category: The created Category object.
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        return super().create(**data)
