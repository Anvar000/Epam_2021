from time import time

from homework3.task2 import calculating_of_total_sum, slow_calculate


def test_calculating_of_total_sum_faster_60_seconds():

    start = time()
    calculating_of_total_sum(slow_calculate, 50, range(500))
    end = time()

    assert end - start < 60
