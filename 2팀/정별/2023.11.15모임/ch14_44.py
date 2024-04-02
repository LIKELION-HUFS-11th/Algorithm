# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if node is None:
            return 0    
    
    def dfs (node: TreeNode):

        left = dfs(node.left)
        rignt = dfs(node.right)
    
    if node.left and node.left.val == node.val:
        left += 1
    else:
        left = 0
    if node.right and node.right.val == node.val:
        right += 1
    else:
        right = 0
