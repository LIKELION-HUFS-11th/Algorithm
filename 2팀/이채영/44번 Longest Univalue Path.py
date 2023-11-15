# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self, result=0):
        self.result = result 
    #함수 내에서 사용 시 local variable 'result' referenced before assignment 라고 오류 발생
    #그러나 result를 반환값으로 쓰기 애매한 상황이므로 따로 매개변수 선언

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else: #바닥까지 도달 - 올라오면서 right값 조정
                right = 0
            self.result = max(self.result, left+right) #함수 밖으로 결과값 전달
            return max(left, right) #하나만 선택해야 함

        
        dfs(root)
        return self.result

        # for i in range(len(root)):
        #     x = root[i]
        #     left_child = root[2*x+1]
        #     right_child = root[2*x+2]
