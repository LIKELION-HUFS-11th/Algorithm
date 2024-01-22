# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root): #루트노드를 기준으로 높이를 부여하는 것임
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)

            if left == -1 or right == -1 or abs(right-left) >1: #양쪽의 서브트리들의 높이차이가 2이상 되는 것도 -1 뱉는 조건. 여기서 높이 차이 계산
                return -1


            return max(left, right) +1 #right과 left 모두 비어있으면, 결국 1출력
                                        #내 자식노드 양측의 높이값(중에서 큰놈)에 1 올라온게 본인 높이임
        
        return check(root) != -1