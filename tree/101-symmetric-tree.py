# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import SimpleQueue

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root.left is None and root.right is None:
            return True

        is_sym = False

        l_queue = SimpleQueue()
        r_queue = SimpleQueue()

        l_queue.put(root.left)
        r_queue.put(root.right)

        while not l_queue.empty() and not r_queue.empty():
            l_node = l_queue.get()
            r_node = r_queue.get()

            if l_node and r_node:
                if l_node.val != r_node.val:
                    is_sym = False
                    break
                else:
                    is_sym = True
            elif l_node is None and r_node is None:
                continue
            else:
                is_sym = False
                break

            if l_node:
                l_queue.put(l_node.left)
                l_queue.put(l_node.right)
            
            if r_node:
                r_queue.put(r_node.right)
                r_queue.put(r_node.left)

        return is_sym
        