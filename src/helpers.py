"""
    helpers
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from functools import wraps, lru_cache


def _make_key(args, kwargs):
    key = args

    for item in sorted(kwargs.items()):
        key += item

    return hash(key)


def simple_cache(func):
    cache = {}

    @wraps(func)
    def _(*args, **kwargs):
        key = _make_key(args, kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    return _
