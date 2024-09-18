from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_elements = set()
        available_position = 0
        count = 0
        for index, elem in enumerate(nums):

            if elem not in unique_elements:
                unique_elements.add(elem)
                nums[available_position] = elem
                available_position += 1
                count += 1

        return count