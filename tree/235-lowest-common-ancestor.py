# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import SimpleQueue

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        queue = SimpleQueue()
        root_obj = ([root], root)
        queue.put(root_obj)
        
        p_found = False
        q_found = False
        p_ancestors = None
        q_ancestors = None

        while queue.empty() == False:
            ancestors, node = queue.get()
            ancestors = ancestors + [node]
            if node.val == p.val:
                p_found = True
                p_ancestors = ancestors
            
            if node.val == q.val:
                q_found = True
                q_ancestors = ancestors

            if p_found and q_found:
                for node in reversed(p_ancestors):
                    if node in q_ancestors:
                        return node

            if node.left:
                queue.put((ancestors, node.left))
            
            if node.right:
                    queue.put((ancestors, node.right))


## Eficient solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import SimpleQueue

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        queue = SimpleQueue()

        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                break
        return root
