"""
Write down the function, which reads input line-by-line, and find
maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    """Function to find the maximimum and the minimum values from the file

    Args:
        file_name (str): path to the file

    Returns:
        Tuple[int, int]: minimum and maximum values
    """
    maximum, minimum = float("-inf"), float("inf")
    with open(file_name) as fi:
        for line in fi:
            number = float(line)
            minimum = min(minimum, number)
            maximum = max(maximum, number)
    return minimum, maximum
