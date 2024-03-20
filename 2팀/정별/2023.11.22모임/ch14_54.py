# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#전위순회 결과와 중위순회 결과 2개로, 기존의 이진트리 복원하기

#일단 정방향으로 처음 트리에서 전위순회 하는 것 시도
[1, 2, 3, 4, 5]
tree = TreeNode()
n = tree.val
l = tree.left
r = tree.right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or inorder:
            return 0
        
        def dfs(r):
            ans_tree = TreeNode()
            root = preorder[0]
            
            while left == inorder[0]:
                left = ans_tree.left 
            rignt = ans_tree.right
        
        

        return ans_tree
        
        
        