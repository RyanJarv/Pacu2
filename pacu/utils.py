"""Utilities module."""
from functools import wraps


def defer_wrap(func):
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        deferred = []
        _defer = lambda dfunc: deferred.append(dfunc)
        try:
            return func(*args, defer=_defer, **kwargs)
        finally:
            deferred.reverse()
            for f in deferred:
                f()
    return func_wrapper
