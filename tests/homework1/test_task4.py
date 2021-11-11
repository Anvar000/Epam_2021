from homework1.task04 import check_sum_of_four


def test_positive():
    """"Test returns = 1 """
    assert check_sum_of_four([0], [0], [0], [0]) == 1


def test_positive_2():
    """"Test returns 6  """
    assert check_sum_of_four([0, 1], [0, -1], [0, 1], [0, -1]) == 6
