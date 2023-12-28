# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # list 조합 -> TreeNode 클래스 형성하기
        # 남아있는 preorder정렬의 가장 첫 값은 루트노드임을 활용 => inorder정렬에서 해당 루트노드보다 앞에 있는 값은 왼쪽부트리, 뒤에 있는 값은 오른쪽부트리임을 활용

        if inorder:
            index = inorder.index(preorder.pop(0)) #루트노드 인덱스 

            node = TreeNode(inorder[index]) #루트노드
            node.left = self.buildTree(preorder, inorder[0:index]) #왼쪽부트리 정렬
            node.right = self.buildTree(preorder, inorder[index+1:]) #오른쪽부트리 정렬 

            return node #null문제 -> TreeNode 클래스로 해결된다.