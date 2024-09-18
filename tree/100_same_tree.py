# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
    def bfs(self, root: TreeNode):
        if root is None:
            return []
        queue = Queue()
        queue.put(root)
        vals = []

        while queue.empty() == False:
            item = queue.get()
            
            left = item.left.val if item.left else None
            right = item.right.val if item.right else None
            t = (item.val, left, right)
            vals.append(t)
            
            if item.left:
                queue.put(item.left)
            if item.right:
                queue.put(item.right)
            
        return vals

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        p_vals = self.bfs(p)
        q_vals = self.bfs(q)


        return p_vals == q_vals
        