from typing import List
"""
Given an array nums of n integers, find all unique triplets in the array which gives the sum of zero.
Source: https://leetcode.com/problems/3sum/
"""


class Solution:
    """
    Time: 28ms and 100%
    Before was 704ms and 90%. The key to the fast speed is computing the end of the outer loop
    using the the `next` function and the terminating if index == 0. Rather than breaking in the
    outer loop when we reach the first positive value.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        index = next(x for x,val in enumerate(nums) if val >0)
        if index == 0 or len(nums) < 3: return result
        for i in range(index):
            # we skip visited beginnings
            if i > 0 and nums[i] == nums[i-1]: continue
            # perform two sum sweep
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = nums[i]+nums[lo]+nums[hi]
                # checking for less than and more than first made it faster
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    while (lo < hi and nums[hi] == nums[hi - 1]):
                        hi -= 1
                    while (lo < hi and nums[lo] == nums[lo + 1]):
                        lo += 1
                    hi -= 1
                    lo += 1
        return result


def tests():
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


tests()
