from collections import deque

n, k = map(int, input().split())

visited = [0] * 1000001
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 1000000 and not visited[nx]:
                visited[nx] = visited[x]+1
                q.append(nx)

bfs()