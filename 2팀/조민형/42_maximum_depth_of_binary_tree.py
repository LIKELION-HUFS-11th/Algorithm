class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 0
        nodes = [root]  # 노드를 리스트로 바꾸기

        while nodes:
            depth += 1
            next_nodes = []  # 다음 레벨의 노드들을 저장할 리스트

            for node in nodes: # 안에서 자식 노드를 탐색하고 추가
                if node.left:
                    next_nodes.append(node.left)
                if node.right:
                    next_nodes.append(node.right)

            nodes = next_nodes  # 다음 레벨의 노드들로 갱신

        return depth
