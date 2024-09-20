# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def dfs(self, root: Optional[TreeNode], sums ) -> int:
        
        if root is None:
            return 0, 0
        
        right_sum_left, right_sum_right = self.dfs(root.right, sums)
        left_sum_left, left_sum_right = self.dfs(root.left, sums)

        right_sum = max(right_sum_left, right_sum_right)
        left_sum = max(left_sum_left, left_sum_right)

        root_sum = root.val

        if right_sum > 0 :
            root_sum = root_sum + right_sum
        if left_sum > 0:
            root_sum = root_sum + left_sum

        sums.append(root_sum)

        return max(root.val, left_sum+root.val), max(root.val, right_sum+root.val)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        self.dfs(root, sums)
        
        return max(sums)

        return max_sum