class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_map = dict()

        for index, number in enumerate(nums):
            diff = target - number
            if diff in number_map:
                return [number_map[diff], index]
            number_map[number] = index