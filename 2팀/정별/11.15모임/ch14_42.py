import collections
#설명 필요
def maxDepth(self, root) -> int:
    
    queue = collections.deque([root])
    depth = 0
    
    while queue:
        depth += 1
        for i in range(len(queue)):
            cur_root = queue.popleft()
            #자식 노드 있는지 판별하고, 해당 자식 노드를 다시 데크에 넣기
            if cur_root.left: #???
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)
        
        
        
    return depth