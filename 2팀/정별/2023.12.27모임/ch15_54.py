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
    def buildTree(self, preorder, inorder):
        if inorder:
            index = inorder.index(preorder.pop(0))
            
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0:index])
            node.right = self.buildTree(preorder, inorder[index +1: ])
            
            return node        
        