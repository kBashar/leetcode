# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import LifoQueue
class Solution:
    def height_diff(self, root: TreeNode):
        if root is None:
            return 0

        left_height = self.height_diff(root.left)
        right_height = self.height_diff(root.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height-right_height) > 1:
            return -1

        return max(left_height, right_height) + 1
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        if self.height_diff(root) == -1:
            return False
        
        return True
        
        