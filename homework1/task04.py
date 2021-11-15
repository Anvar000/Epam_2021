"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] +
    B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from itertools import product
from typing import Dict, List


def check_sum_of_four(a: List[int], b: List[int], c: List[int],
                      d: List[int]) -> int:
    """
    Given four lists a, b, c, d of integer values.
    Function computes how many tuples (i, j, k, l) there are such
    that A[i] + B[j] + C[k] + D[l] is zero.

    Args:
        a: List[int]
        b: List[int]
        c: List[int]
        d: List[int]

    Returns:
        count: int
    """
    sum_a_b: Dict[int, int] = {}
    for item in product(a, b):
        sum_a_b[sum(item)] = sum_a_b.get(sum(item), 0) + 1

    sum_c_d: Dict[int, int] = {}
    for item in product(c, d):
        sum_c_d[sum(item)] = sum_c_d.get(sum(item), 0) + 1

    count: int = 0
    for key in sum_a_b:
        if sum_c_d.get(-key):
            count += sum_a_b.get(key, 0) * sum_c_d.get(key, 0)

    return count
