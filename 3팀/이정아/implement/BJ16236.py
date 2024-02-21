from collections import deque
import heapq

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
edible = []
sec = 0
size = 2
dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ate = 0
candidate = deque()

for i in range(n):
    for j in range(n):
        if 0 < arr[i][j] < size:
            edible.append((i, j))
        if arr[i][j] == 9:
            now = (i, j)
            arr[i][j] = 0
            edible.append((i, j))

candidate.append((0, now[0], now[1]))
    
def add_edible():
    for i in range(n):
        for j in range(n):
            if 0 < arr[i][j] < min(size, 8) and (i, j) not in edible:
                edible.append((i, j))

def bfs(a, b):
    global sec
    global candidate
    global ate
    q = deque()
    q.append((a, b))
    dist = [[0] * n for _ in range(n)]
    cand = []
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dxy[i][0], y + dxy[i][1]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == 0 and arr[nx][ny] <= size:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
                if (nx, ny) in edible:
                    heapq.heappush(cand, (dist[nx][ny], nx, ny))
    if len(cand) > 0:
        candidate.append(heapq.heappop(cand))
        return True
    return False

if len(edible) == 0:
    print(0)
else:
    while candidate:
        time, x, y = candidate.popleft()
        sec += time
        arr[x][y] = 0
        edible.remove((x, y))
        if bfs(x, y):
            ate += 1
            if ate == size:
                size += 1
                ate = 0
            add_edible()
            continue
        else:
            break
    print(sec)

