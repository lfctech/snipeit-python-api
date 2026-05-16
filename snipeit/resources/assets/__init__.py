"""Assets package — re-exports Asset and AssetsManager for back-compat."""

from .manager import AssetsManager
from .model import Asset

__all__ = ["Asset", "AssetsManager"]
