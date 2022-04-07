"""Externally-accessible endpoint handlers that serve relative to
``/<app-name>/``.
"""

__all__ = [
    "get_index",
    "get_recent_table",
    "events",
    "current",
]
from rubintv.handlers.external.endpoints import current, events, get_recent_table
