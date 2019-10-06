
from typing import List
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
Source: https://leetcode.com/problems/two-sum/
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_nums = {}
        for i, n in enumerate(nums):
            if n in prev_nums:
                return [prev_nums[n], i]
            prev_nums[target - n] = i
        return [-1, -1]


def tests():
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]


tests()
