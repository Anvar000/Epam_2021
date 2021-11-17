"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g')
== ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p')
== ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2)
== ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(data, *args):
    """function that accept any iterable of unique values and then
    it behaves as range function

    Args:
        data ([type]): iterable of unique values
        args: start
              start, stop
              start, stop, step

    Example:
    assert = custom_range(string.ascii_lowercase, 'g') ==
                        ['a', 'b', 'c', 'd', 'e', 'f']
    assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
                        ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
    assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
                        ['p', 'n', 'l', 'j', 'h']
    """
    if len(args) == 1:
        return list(data[: data.index(args[0])])
    if len(args) == 2:
        return list(data[data.index(args[0]): data.index(args[1])])
    if len(args) == 3:
        return list(data[data.index(args[0]): data.index(args[1]): args[2]])
    if len(args) > 3:
        raise TypeError(f"custom_range expects no more than 3 args,\
            got {len(args)}")
