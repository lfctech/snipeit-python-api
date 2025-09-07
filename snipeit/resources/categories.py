from typing import Any, Dict, List
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
        data = {"name": name, "category_type": category_type}
        data.update(kwargs)
        return super().create(**data)
