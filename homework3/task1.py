"""
In previous homework task 4, you wrote a cache function that remembers
other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use
 aw_input() instead

    >>> f()
    ? 1
    '1'
    >>> f()     # will remember previous value
    '1'
    >>> f()     # but use it up to two times only
    '1'
    >>> f()
    ? 2
    '2'
"""
from typing import Callable


def cache(times):
    """Return function with cashing results.
    Caches 'times' results of calls
    """
    def cacher(function: Callable) -> Callable:
        journal = {}

        def wrapper(*args, **kwargs):
            args_mod = tuple(str(i) for i in args)
            kwargs_mod = tuple(str(i) for i in kwargs.items())
            all_args = args_mod, kwargs_mod
            if journal.get(all_args) and journal.get(all_args)[1] > 0:
                result = journal.get(all_args)[0]
                journal[all_args][1] -= 1
            else:
                result = function(*args, **kwargs)
                journal[all_args] = [result, times]
            return result

        return wrapper

    return cacher


if __name__ == "__main__":

    @cache(times=2)
    def func(a, b, c=0, d=0):
        return (a ** b) ** 2 + c + d

    some = 10, 2

    val_1 = func(*some, c=2, d=3)
    print(f"{val_1=}")
    val_1 = func(*some, c=4, d=5)
    print(f"{val_1=}")
    val_1 = func(*some, c=4, d=5)
    print(f"{val_1=}")
    val_1 = func(*some, c=4, d=5)
    print(f"{val_1=}")
