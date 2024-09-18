class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        dups = []
        prev = nums[0]
        for n in nums[1:]:
            if n == prev:
                dups.append(n)
            prev = n
        return dups