class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_map = dict()

        for index, number in enumerate(nums):
            diff = target - number
            if diff in number_map:
                return [number_map[diff], index]
            number_map[number] = index


sol = Solution()
assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
assert sol.twoSum([3, 2, 4], 6) == [1, 2]
assert sol.twoSum([3, 3], 6) == [0, 1]
