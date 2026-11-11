import functools
import warnings
from typing import Callable


def _deprecated(hint: str, removed: bool = False) -> Callable:
    """The decorator marks a method as deprecated and emits a DeprecationWarning for every call.

    Args:
        hint (str): Specify the hint that explains what to use instead
        removed (bool): Specify if Grafana removed the corresponding endpoint, so the call fails on recent Grafana versions (default False)

    Returns:
        decorator (Callable): Returns the decorator that wraps the deprecated method

    """

    def decorator(func: Callable) -> Callable:
        reason: str = " and the Grafana endpoint was removed in recent versions" if removed else ""
        message: str = f"{func.__qualname__} is deprecated{reason}, {hint}."

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(message, DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)

        return wrapper

    return decorator
