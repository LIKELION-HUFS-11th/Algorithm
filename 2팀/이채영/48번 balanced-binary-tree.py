# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def binary_tree(node):
            if not node.left and not node.right:
                return 0

            left = binary_tree(node.left)
            right = binary_tree(node.right)

            if node.left:
                left += 1
            if node.right:
                right += 1

            if left == False or right == False or abs(right - left) > 1:
                return False
            else:
                return max(left, right)

        satisfied = binary_tree(root)
        if satisfied == False:
            return False
        else:
            return satisfied
            

        