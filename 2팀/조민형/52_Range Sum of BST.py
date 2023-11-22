# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #재귀적으로 사용할 함수 정의
        def dfs(root:TreeNode):
            if not root:
                return 0

            #low보다 작을 때는 오른쪽으로 가야 해당 범위 안으로 진입할 수 있기 때문에 오른쪽 서브트리를 dfs
            if root.val < low :
                return dfs(root.right)
            #high보다 클 때는 왼쪽으로 가야 해당 범위 안으로 진입할 수 있기 때문에 왼쪽 서브트리를 dfs
            elif root.val > high:
                return dfs(root.left)
            #해당 조건들을 지나친다면 조건에 부합한다는 뜻이므로 해당 val 값을 더하고 계속해서 dfs로 더 있는지 탐색
            return root.val + dfs(root.left) + dfs(root.right)

        return dfs(root) 

        
        