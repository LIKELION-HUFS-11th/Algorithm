# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # def __init__(self, tree=TreeNode()):
    #     self.tree = tree
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """

        # def merge(node1, node2):
        #     self.tree.val = 0 ###'NoneType' object has no attribute 'val'
        #     if node1 == None and node2 == None:
        #         return
            
        #     if node1 == None:
        #         self.tree.val = node1.val
        #     if node2 == None:
        #         self.tree.val = node2.val
        #     if node1 and node2:
        #         self.tree.val = node1.val + node2.val
            
        #     self.tree = self.tree.left
        #     merge(node1.left, node1.right)
        #     self.tree = self.tree.right
        #     merge(node1.right, node2.right)
        
        # merge(root1, root2)
        # return tree


        if root1 and root2:
            node = TreeNode(root1.val + root2.val) #새로운 TreeNode객체를 생성
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
        
            return node
        else:
            return root1 or root2 #A,B 중 하나만 참이라면 참인 값을 반환
            #참고로 and 사용 시 그 반대