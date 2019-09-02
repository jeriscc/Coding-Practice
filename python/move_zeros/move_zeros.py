from typing import List

class Solution:
    def moveZeros(self, nums: List[int]):
        i = 0
        j = 0

        while i < len(nums):
            if nums[i] != 0:
                temp = nums[j]
                nums[j] = nums[i]
                nums[i] = temp
                j += 1
            i += 1