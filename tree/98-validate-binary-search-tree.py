from typing import List

class Solution:

    def dfs(self, root: Optional[TreeNode], nums: List[int]):

        if root is None:
            return []
        
        new_nums = self.dfs(root.left, nums) + [root.val]

        return new_nums + self.dfs(root.right, nums)
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        all_nums = self.dfs(root, [])
        prev = all_nums[0]
        for n in all_nums[1:]:
            if n <= prev:
                return False
            prev = n
        return True

        
