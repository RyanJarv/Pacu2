"""Utilities module."""
import base64
import hashlib
import json
import os
from copy import copy
from datetime import datetime
from functools import wraps
from itertools import chain
from typing import Callable, List, Optional

from ratelimit import sleep_and_retry, limits

from pacu.settings import app_dir


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


def limit_requests(reqs_second: int = 0):
    """Returns a function that blocks if called more then 'reqs_second' times a second."""

    @sleep_and_retry
    @limits(reqs_second, 1)
    def _limit_requests(*args, **kwargs):
        pass

    return _limit_requests


def pcache(ignore_args: List[str] = None, ignore_kwargs: List[str] = None):
    def arg_wrapper(func: Callable):
        def _wrapper(*args, **kwargs):
            hargs, hkwargs = list(copy(args)), list(copy(kwargs))
            if ignore_args is not None:
                for i in ignore_args:
                    del hargs[i]
            if ignore_kwargs is not None:
                for i in ignore_args:
                    del hkwargs[i]
            argstr = json.dumps({'args': hargs, 'kwargs': hkwargs}, default=str)
            m = hashlib.sha256()
            m.update(argstr.encode())
            path = app_dir / 'cache' / func.__name__ / f"{base64.b64encode(m.digest()).decode().replace('/', '_')}.json"
            if path.is_file():
                return json.loads(path.read_text())
            os.makedirs(path.parent, exist_ok=True)
            resp = func(*args, **kwargs)
            path.write_text(json.dumps(resp, default=str))
            return resp
        return _wrapper
    return arg_wrapper
