"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """
    Function returns the maximal sum of sub-array with length less
    equal k of given list.

    Args:
        nums:  List[int] - list of integers numbers
        k: int - sub-array length

    Returns:
        maximal_sum_of_subarray: int
    """
    if not nums or k == 0:
        return 0
    max_sum = nums[0]
    for i, _ in enumerate(nums):
        check_sum = 0
        for element in nums[i: i + k]:
            check_sum += element
            if check_sum > max_sum:
                max_sum = check_sum

    return max_sum
