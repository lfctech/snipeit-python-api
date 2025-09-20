"""Categories resources.

Provides Category model and CategoriesManager for Snipe-IT categories.
"""

from typing import Any
from .base import ApiObject, BaseResourceManager


class Category(ApiObject):
    """Represents a Snipe-IT category.

    Examples:
        Fetch a category and display it:

            cat = api.categories.get(1)
            print(cat)
    """
    _path = "categories"

    def __repr__(self) -> str:
        """Return a concise string representation.

        Returns:
            str: The category id, name, and type.
        """
        return f"<Category {getattr(self, 'id', 'N/A')}: {getattr(self, 'name', 'N/A')} (Type: {getattr(self, 'category_type', 'N/A')})>"


class CategoriesManager(BaseResourceManager[Category]):
    """Manager for Category-related API operations.

    Examples:
        Create a category:

            api.categories.create(name="Laptops", category_type="asset")
    """

    resource_cls = Category
    path = Category._path

    def create(self, name: str, category_type: str, **kwargs: Any) -> 'Category':
        """Create a new category.

        Args:
            name (str): The name of the category.
            category_type (str): The type of the category.
            **kwargs: Additional fields for the category.

        Returns:
            Category: The created Category object.

        Examples:
            Create a printers category:

                api.categories.create(name="Printers", category_type="asset")
        """
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        return super().create(**data)
