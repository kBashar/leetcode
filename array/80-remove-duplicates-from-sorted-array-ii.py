class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0
        prev = nums[0]
        count = 0
        k = len(nums)

        while r < len(nums):
            if nums[r] == prev:
                count += 1
            else:
                count = 1
                prev = nums[r]
            if count > 2:
                 k -= 1 
            else:
                nums[l] = nums[r]
                l += 1
            r += 1
        return k