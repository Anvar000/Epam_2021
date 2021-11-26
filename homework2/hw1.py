"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import string
from typing import Counter, Dict, List

import regex as re


def get_longest_diverse_words(file_path: str) -> List[str]:
    """Function to find the 10 longest words consisting from largest
    amount of unique symbols from the document.

    Args:
        file_path (str): the path of the file

    Returns:
        List[str]: list of 10 longest words consisting from largest
    amount of unique symbols
    """
    words_with_info = {}
    with open(file_path, mode='r',
              encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            line = line.lower()
            line = re.sub(r"\p{P}+", "", line)
            line = re.sub(r"[0-9]", " ", line)
            for word in line.split():
                words_with_info[len(set(word))] = word
    sorted_words_by_info = sorted(list(words_with_info.items()), reverse=True)

    return [item[1] for item in sorted_words_by_info[:10]]


def get_rarest_char(file_path: str) -> str:
    """Find the rarest symbol for the document

    Args:
        file_path (str): the path of the file

    Returns:
        str: the rarest chatacter from the file
    """
    counts_of_chars: Dict[str, int] = {}
    with open(file_path, mode='r',
              encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for ch in line:
                counts_of_chars[ch] = counts_of_chars.get(ch, 0) + 1
    sorted_tuples = sorted(counts_of_chars.items(), key=lambda item: item[1])

    return sorted_tuples[0][0]


def count_punctuation_chars(file_path: str) -> int:
    """Function count the number of the punctuations

    Args:
        file_path (str): the path of the file

    Returns:
        int: the number of the punctuations
    """
    count_of_punctuation = 0
    with open(file_path, mode='r',
              encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:
                if char in string.punctuation:
                    count_of_punctuation += 1

    return count_of_punctuation


def count_non_ascii_chars(file_path: str) -> int:
    """Function count every non ascii char

    Args:
        file_path (str): the path of the file

    Returns:
        int: the number of the non ascii chars
    """
    count_non_ascii = 0
    with open(file_path, mode='r',
              encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:
                if not char.isascii():
                    count_non_ascii += 1

    return count_non_ascii


def get_most_common_non_ascii_char(file_path: str) -> str:
    """Function to find most common non ascii char for the document

    Args:
        file_path (str): the path of the file

    Returns:
        str: the most common non ascii char for the document
    """
    non_ascii_chars = Counter()
    with open(file_path, mode='r',
              encoding='unicode-escape',
              errors='ignore') as file:
        for line in file:
            for char in line:
                if not char.isascii():
                    non_ascii_chars[char] += 1

    return non_ascii_chars.most_common()[0][0]
