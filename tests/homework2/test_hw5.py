import string

from homework2.hw5 import custom_range


def test_one_args_stop():
    correct_res = ["a", "b", "c", "d", "e", "f"]
    assert correct_res == custom_range(string.ascii_lowercase, "g")


def test_two_args_start_stop():
    correct_res = ["g", "h", "i", "j", "k", "l", "m", "n", "o"]
    assert correct_res == custom_range(string.ascii_lowercase, "g", "p")


def test_three_args_start_stop_step():
    correct_res = ["p", "n", "l", "j", "h"]
    assert correct_res == custom_range(string.ascii_lowercase, "p", "g", -2)
