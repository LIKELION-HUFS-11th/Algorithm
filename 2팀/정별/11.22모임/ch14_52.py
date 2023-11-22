# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        cnt = 0
        def dfs(root_n):
            nonlocal cnt
            if not root_n:
                return None
            
            if low<= root_n.val and root_n.val <= high:
                cnt += root_n.val

            l = dfs(root_n.left)
            r = dfs(root_n.right)
            return cnt
        
        return dfs(root)
