"""Data models and utilities for meshed surfaces."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("morphosurfaces")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Kevin Yamauchi"
__email__ = "kevin.yamauchi@gmail.com"
