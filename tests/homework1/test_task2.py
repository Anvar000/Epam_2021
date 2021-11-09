from homework1.task02 import check_fibonacci


def test_empty_list():
    assert check_fibonacci([]) is False


def test_fib_sequence():
    assert check_fibonacci([0, 1, 1, 2, 3, 5, 8, 13])


def test_not_fib_sequence():
    assert check_fibonacci([1, 2, 3, 4]) is False


def test_only_zero():
    assert check_fibonacci([0]) is False
