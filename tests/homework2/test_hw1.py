import os

from homework2.hw1 import (count_non_ascii_chars, count_punctuation_chars,
                           get_longest_diverse_words,
                           get_most_common_non_ascii_char, get_rarest_char)


def test_get_longest_diverse_words():
    file_path = os.path.dirname(__file__) + "/hw1/test_data.txt"
    assert get_longest_diverse_words(file_path) == [
        'betrachtung',
        'ausführen',
        'bedenkli',
        'sondern',
        'grenzen',
        'wird',
        'hin',
        'es',
        '—']


def test_get_rarest_char():
    file_path = os.path.dirname(__file__) + "/hw1/test_data.txt"
    assert get_rarest_char(file_path) == 'S'


def test_count_punctuation_chars():
    file_path = os.path.dirname(__file__) + "/hw1/test_data.txt"
    assert count_punctuation_chars(file_path) == 7


def test_count_non_ascii_chars():
    file_path = os.path.dirname(__file__) + "/hw1/test_data.txt"
    assert count_non_ascii_chars(file_path) == 9


def test_get_most_common_non_ascii_char():
    file_path = os.path.dirname(__file__) + "/hw1/test_data.txt"
    assert get_most_common_non_ascii_char(file_path) == 'ü'
