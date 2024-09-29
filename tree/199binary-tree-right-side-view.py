# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import LifoQueue

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        r_nodes = []
        
        if root is None:
            return r_nodes
        
        level_nodes = [root]
        
        while len(level_nodes) > 0:
            next_level_nodes = []
            
            for node in level_nodes:
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            
            r_nodes.append(level_nodes[-1].val)
            
            level_nodes = next_level_nodes
    
        return r_nodes

