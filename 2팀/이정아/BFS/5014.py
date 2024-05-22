from collections import deque

highest, now, target, up, down = map(int, input().split())
visited = [float('inf')] * (highest+1)
q = deque()
q.append(now)
visited[now] = 0

while q:
    x = q.popleft()
    if x == target:
        print(visited[x])
        break
    if x+up <= highest and visited[x+up] > visited[x]+1:
        q.append(x+up)
        visited[x+up] = visited[x]+1
    if x-down > 0 and visited[x-down] > visited[x]+1:
        q.append(x-down)
        visited[x-down] = visited[x]+1
        
if visited[target] == float('inf'):
    print("use the stairs")