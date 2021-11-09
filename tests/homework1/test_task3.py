import os

from homework1.task03 import find_maximum_and_minimum


def test_file_with_only_one_value():
    file_path = os.path.dirname(__file__) + "/task3_test_files/test1.txt"
    assert find_maximum_and_minimum(file_path) == (5.0, 5.0)


def test_file_with_two_equal_values():
    file_path = os.path.dirname(__file__) + "/task3_test_files/test2.txt"
    assert find_maximum_and_minimum(file_path) == (-15.0, -15.0)


def test_file_with_different_values():
    file_path = os.path.dirname(__file__) + "/task3_test_files/test3.txt"
    assert find_maximum_and_minimum(file_path) == (-100.0, 100.1)
