import sys
from typing import Any
from collections.abc import Callable

if sys.version_info < (3, 10):
    # compatibility for python <3.10
    import importlib_metadata as metadata
else:
    from importlib import metadata

try:
    VERSION_TYPE = Callable[[str], str]
except TypeError:
    VERSION_TYPE = Any  # type: ignore

version: VERSION_TYPE = metadata.version

__version__ = version("aio-clients")
