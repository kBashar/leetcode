from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        
        for index in range(len(nums)):

            suffix = 1
            prefix = 1

            for i in range(0, index):
                suffix *= nums[i]
            
            for i in range(len(nums)-1, index, -1):
                prefix *= nums[i]
            
            answer.append(suffix * prefix)
        return answer


if __name__ == "__main__":
    sol = Solution()
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24,12,8,6]
    assert sol.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]