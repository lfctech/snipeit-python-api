"""snipeit package.

Provides the primary SnipeIT client for interacting with the Snipe-IT API.

Examples:
    Basic usage:
        from snipeit import SnipeIT
        with SnipeIT(url="https://example.test", token="{{SNIPEIT_API_TOKEN}}") as api:
            asset = api.assets.get(1)
            print(asset)
"""

from .client import SnipeIT
__all__ = ["SnipeIT"]
