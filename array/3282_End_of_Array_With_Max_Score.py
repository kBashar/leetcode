class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        i = 0
        score = 0

        for j in range(1, len(nums)):
            if nums[j] > nums[i]:
                score += (j - i) * nums[i]
                i = j
            elif j == len(nums)-1:
                score += (j - i) * nums[i]
        
        return score
            
