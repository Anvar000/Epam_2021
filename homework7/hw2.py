"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def format_text(text: str) -> list:
    """Function to represent string without #

    Args:
        text (str): text with symbol backspace #

    Returns:
        result (list): the saved list of symbols after
                       the formating text with backspace
    """
    result = []
    for i in range(0, len(text)):
        if text[i] == "#":
            if result:
                result.pop()
        else:
            result.append(text[i])
    return result


def backspace_compare(first: str, second: str) -> bool:
    """Compare the two strings after the representing two strings
    Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

    Args:
        first (str): first string with symbol #
        second (str): second string with symbol #

    Returns:
        bool: true if both of strings equal after editing
              false otherwise
    """
    return format_text(first) == format_text(second)
