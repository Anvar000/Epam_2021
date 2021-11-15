"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    """This function check is the given data the sequence of the Fibonacci or not

    Args:
        data (Sequence[int]): given data as the list of integer numbers

    Returns:
        bool: True - if the given data is the sequence of the Fibonacci
              False - on the other cases
    """

    if not data:
        return False
    if len(data) > 2 and data[0] == 0 and data[1] == 1:
        first = data[0]
        second = data[1]
        for element in data[2:]:
            if first + second != element:
                return False
            first, second = second, element
        return True
    return False
