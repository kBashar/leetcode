class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_map = {}

        for index, num in enumerate(nums):
            if num in num_map:
                prev_idx = num_map[num]
                if k >= index - prev_idx:
                    return True
            num_map[num] = index
        return False


sol = Solution()
assert sol.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
assert sol.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
assert sol.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
