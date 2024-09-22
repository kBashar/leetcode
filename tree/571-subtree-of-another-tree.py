# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import SimpleQueue

class Solution:
    
    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        elif root is None or subRoot is None:
            return False
        elif root.val == subRoot.val:
            right_match = self.dfs(root.right, subRoot.right)
            left_match = self.dfs(root.left, subRoot.left)

            return right_match and left_match
        else:
            return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = SimpleQueue()

        queue.put(root)

        while queue.empty() == False:
            node = queue.get()

            if node.val == subRoot.val:
                matched = self.dfs(node, subRoot)

                if matched:
                    return True

            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        
        return False
