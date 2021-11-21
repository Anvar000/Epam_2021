"""
Armstrong number is a number that is the sum of its own digits each raised
to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong
number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> bool:
    """Check is a given number the Artmstrong number

    Args:
        number (int): the number to check

    Returns:
        bool: True - A number is the Artmstrong number
              False - A number is not the Artmstrong number
    """
    result = False
    number_str = str(number)
    elem = [i for i in number_str]
    a = map(lambda i: int(i) ** len(number_str), elem)
    summ = sum(a)
    if summ == number:
        result = True
    return result


assert is_armstrong(153) is True, 'Is Armstrong number'
assert is_armstrong(10) is False, 'Is not Armstrong number'