# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import LifoQueue

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        nodes = []

        if root is None:
            return nodes

        stack = LifoQueue()
        stack.put([root])

        while stack.empty() == False:
            level_nodes = []
            next_level = []
            for node in stack.get():
                if node is None:
                    continue
                level_nodes.append(node.val)
                next_level.append(node.left)
                next_level.append(node.right)
            if level_nodes:
                nodes.append(level_nodes)
            if next_level:
                stack.put(next_level)
        return nodes
