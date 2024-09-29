# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self, root: Optional[TreeNode], k: int, l: List[int]):
        if len(l) == k:
            return l
        
        if root.left:
            l = self.dfs(root.left, k, l)
        l.append(root.val)
        if root.right:
            l = self.dfs(root.right, k, l)
        return l
        


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        l = self.dfs(root, k, [])

        return l[k-1]