### 알고스팟

m, n = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]


import heapq

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
distances = [ [float('inf')]*m  for _ in range(n)]


def dijkstra(x, y):
    distances[x][y] = 0

    priority_queue = [(0, x, y)]

    while priority_queue:
        wall, x, y = heapq.heappop(priority_queue)

        if x == n-1 and y == m-1:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                tmp_wall = wall + maze[nx][ny]
                if distances[nx][ny] > tmp_wall:
                    distances[nx][ny] = tmp_wall
                    heapq.heappush(priority_queue, (tmp_wall, nx, ny))

    return distances


ans = dijkstra(0, 0)

print(ans[n-1][m-1])