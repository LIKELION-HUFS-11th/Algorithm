import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

'''
n: 수빈이 위치
k: 동생 위치
'''
visited = [0] * (100001)

def bfs(s):
    q = deque()
    q.append(s)

    while q:
        n = q.popleft()

        if n == k:
            return visited[n]
        
        for i in [n - 1, n + 1, 2 * n]:  # 뒤로 걷기, 앞으로 걷기, 순간이동
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[n] + 1
                q.append(i)
    
print(bfs(n))