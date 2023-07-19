# n, k 입력
n, k = map(int, input().split())
# lab
lab = [
    list(map(int, input().split()))
    for _ in range(n)
]
# s, r, c 입력
s, r, c = map(int, input().split())

# 함수들
# in_range(x, y)
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# can_spread
def can_spread(x, y):
    # 방문한 적 없고, 범위 내에 있으면 가능
    return in_range(x, y) and not visited[x][y]

# bfs
def bfs():
    t = 0
    while q:
        
        if t == s:
            break

        dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
        for _ in range(len(q)):
            virus_num, x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if can_spread(nx, ny):
                    lab[nx][ny] = lab[x][y]
                    visited[nx][ny] = True
                    q.append((virus_num, nx, ny))
        t += 1

# 설계
# 큐 사용 준비
from collections import deque
q = deque()

# virus (번호, x, y)
virus = []
for i in range(n):
    for j in range(n):
        if lab[i][j]:
            virus.append((lab[i][j], i, j))
# 정렬 (번호가 낮은 종류의 바이러스부터 증식)
virus.sort()

# visited
visited = [
    [0] * n
    for _ in range(n)
]

# bfs 준비
for v in virus:
    # unpacking
    virus_num, x, y = v
    visited[x][y] = True
    q.append(v)

# bfs
bfs()

# 출력
print(lab[r-1][c-1])