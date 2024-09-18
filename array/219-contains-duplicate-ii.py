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