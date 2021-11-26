"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from typing import Callable


def cache(func: Callable) -> Callable:
    """Return function with cashing results"""
    stored_values = {}

    def wrapper(*args, **kwargs):
        all_arguments = (args, tuple(sorted(kwargs.items())))
        if all_arguments not in stored_values:
            stored_values[all_arguments] = func(*args, **kwargs)
            return stored_values[all_arguments]

    return wrapper
