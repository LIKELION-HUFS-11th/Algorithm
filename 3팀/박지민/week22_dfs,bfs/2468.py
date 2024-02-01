# 입력 받기
N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

# 함수
def dfs(x, y, height, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 현재 위치를 방문 처리
    visited[x][y] = True

    # 주변 지점에 대해 탐색 진행
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and area[nx][ny] > height:
            dfs(nx, ny, height, visited)

def count_safe_areas(height):
    # 높이가 height 이하인 지점을 잠기게
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and area[i][j] > height:
                dfs(i, j, height, visited)
                count += 1

    return count

# 높이의 최소값과 최대값 
min_height, max_height = min(map(min, area)), max(map(max, area))

# 최대 안전 영역 개수
max_safe_areas = 0
for height in range(min_height, max_height + 1):
    max_safe_areas = max(max_safe_areas, count_safe_areas(height))

print(max_safe_areas)