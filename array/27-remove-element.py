from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        current_position = 0
        browse_position = 0
        removal_count = 0
        for index, _ in enumerate(nums):
            if nums[index] != val:
                nums[current_position] = nums[browse_position]
                current_position += 1
                browse_position += 1
            else:
                browse_position += 1
                removal_count += 1
        return len(nums) - removal_count