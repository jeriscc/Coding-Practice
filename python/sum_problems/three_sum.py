from typing import List
"""
Given an array nums of n integers, find all unique triplets in the array which gives the sum of zero.
Source: https://leetcode.com/problems/3sum/
"""


class Solution:
    """
    Time: 28ms and 100%
    Before was 704ms and 90%. The reason of the fast speed is computing the end of the outer loop
    using the the `next` function and the terminating if index == 0. Rather than breaking in the
    outer loop when we reach the first positive value.

    Fidelled with code more. Seems like the reason why it was so fast has to do with the `next` function
    throwing the StopIteration error when it can't find a positive number. When we catch the StopIteration
    or prevent it from ever happening, the running time shoots up too around 700.

    Decided to handle the StopIteration Error and now the runtime is 716ms and 88%.
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        nums = sorted(nums)

        if nums[0] > 0 or nums[-1] < 0:
            return []
        if nums[0] == 0: return [[0,0,0]] if nums[2] == 0 else []
        # if the next line is commented out, or if we don't handle the case when the last
        # is 0 but no solution exists, the runtime goes down to around 30ms
        if nums[-1] == 0: return [[0,0,0]] if nums[-3] == 0 else []

        index = next(x for x, val in enumerate(nums) if val > 0)
        result = []
        for i in range(index):
            # we skip visited beginnings
            if i > 0 and nums[i] == nums[i-1]:
                continue
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
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]


tests()
