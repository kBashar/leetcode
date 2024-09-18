from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        contiguous_sum = nums[0]
        for i in range(1,len(nums)):
            contiguous_sum = max(contiguous_sum + nums[i], nums[i])
            max_sum = max(contiguous_sum, max_sum)
        return max_sum