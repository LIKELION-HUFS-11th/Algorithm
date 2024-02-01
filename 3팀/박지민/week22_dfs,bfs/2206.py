from collections import deque

# 입력
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

# 함수
def shortest_path(N, M, maze):
    # 상, 하, 좌, 우 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 방문 여부 및 벽을 부순 횟수를 기록하는 배열
    visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

    # 시작점부터 BFS 시작
    queue = deque([(0, 0, 1)])  # (x, y, 부순 벽의 개수)
    visited[0][0][1] = True

    while queue:
        x, y, can_break = queue.popleft()

        # 목적지에 도달한 경우 최단 경로 반환
        if x == N - 1 and y == M - 1:
            return visited[x][y][can_break]

        # 상하좌우 이동
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 맵 범위 체크
            if 0 <= nx < N and 0 <= ny < M:
                # 이동 가능한 경우
                if maze[nx][ny] == 0 and not visited[nx][ny][can_break]:
                    visited[nx][ny][can_break] = visited[x][y][can_break] + 1
                    queue.append((nx, ny, can_break))
                # 벽을 부수고 이동하는 경우
                elif maze[nx][ny] == 1 and can_break:
                    visited[nx][ny][0] = visited[x][y][can_break] + 1
                    queue.append((nx, ny, 0))

    # 도달할 수 없는 경우
    return -1

# 최단 경로 출력
result = shortest_path(N, M, maze)
print(result)
