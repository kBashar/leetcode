# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root: Optional[TreeNode], max_d: int = 0):
        if root is None:
            return 0, 0

        left_contribution, max_l_d = self.dfs(root.left, max_d)
        right_contribution, max_r_d = self.dfs(root.right, max_d)

        diameter = left_contribution + right_contribution

        contribution = max(left_contribution, right_contribution) + 1

        max_d = max(max_l_d, max_r_d, diameter)


        return contribution, max_d

               

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        contribution, max_d = self.dfs(root)
        return max_d