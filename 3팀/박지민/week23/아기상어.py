from heapq import heappop, heappush

n = int(input())
fish = [list(map(int, input().split())) for _ in range(n)]
cur_x, cur_y = 0, 0 # 현재 위치를 왜 원점으로 시작하는 거지?
cur_fish = 2 # 현재 크기 = 현재 물고기 수로 한듯
cnt = 0
dxy = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 최단 거리에 있는 물고기 찾는 함수
def find_shortest_route(i, j):
    h = [] #비어있는 리스트
    heappush(h, (0, i, j)) # 힙에 아기상어 위치 넣어줌
    visited = [[0]*n for _ in range(n)] #방문처리 리스트
    visited[i][j] = 1
    check, cx, cy = float('inf'), 100, 100 #가장 상단의 가장 왼쪽이니까 최솟값
    # 최솟값 구하려면 무한으로 초기화 필요
    while h:
        c, x, y = heappop(h) #힙에서 빼면 0, 현재위치
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and not visited[nx][ny] and fish[nx][ny] <= cur_fish:
                visited[nx][ny] = c + 1 #나라면 c+1안 하고 그냥 1할 것 같은데.. 왜지?
                # check : 현재까지의 최단거리보다 크면 갱신 못하고 반환
                if visited[nx][ny] > check:
                    return cx, cy, check
                # 최단거리보다 작으면서 먹을 수 있는 칸이고
                if 1 <= fish[nx][ny] < cur_fish:
                    # 이동한 위치의 좌표가 원래 최단 위치보다 왼쪽 상단이면
                    if nx < cx or (nx == cx and ny < cy):
                        # 최단거리와 최단거리의 좌표를 갱신
                        check, cx, cy = visited[nx][ny], nx, ny
                    else:
                        continue
                heappush(h, (visited[nx][ny], nx, ny))
    return cx, cy, check

for i in range(n):
    for j in range(n):
        # 아기상어 위치 찾아서 cur_x, cur_y에 저장하고
        if fish[i][j] == 9:
            cur_x, cur_y = i, j 
        # 먹을 수 있는 물고기가 한 마리면 그 물고기를 먹으러 가므로
        if fish[i][j] > 0 and fish[i][j] < 2:
            # 그냥 먹은 물고기 수 +1 해주면 됨
            cnt += 1

if cnt == 0:
    print(0)
# 먹을 물고기가 한 마리 이상이면
else:
    eat = 0 #먹은 물고기 수
    result = 0
    # 
    while True:
        if eat == cur_fish:
            eat = 0 #먹은 물고기 수를 0으로 리셋 -> 왜?
            cur_fish += 1 #크기 증가
        fish[cur_x][cur_y] = 0 #먹었으니 0으로 바꿔줌
        cur_x, cur_y, r = find_shortest_route(cur_x, cur_y)
        # 더 이상 먹을 물고기가 없다면
        if cur_x == 100:
            break
        result += r # 최단 경로 거리 r, 즉 물고기까지 이동하는 시간 더해줌
        eat += 1 # eat = 현재 크기의 먹이를 몇 마리 먹었는지
    
    print(result)








