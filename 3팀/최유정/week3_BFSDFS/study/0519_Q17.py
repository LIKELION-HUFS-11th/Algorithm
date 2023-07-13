# 경쟁적 전염

from collections import deque

N, K = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def find(map_list):
    virus = []
    for i in range(N):
        for j in range(N):
            if map_list[i][j] == 0: continue
            virus.append([map_list[i][j], i, j]) # 바이러스 크기, 바이러스 위치(i, j) 담기
    virus.sort() # 크기가 작은 순으로 정렬
    return deque(virus)


def bfs(map_list):
    virus = find(map_list)
    check, vs, cnt = 0, len(virus), 0 # check : 몇 개의 바이러스를 체크했는지, vs : 한 서클 내에 있는 바이러스 수, cnt : 몇 서클인지

    while virus:
        if cnt == S: break
        if check == vs: # 한 서클을 돌았는지
            cnt += 1 # 1초 추가
            check, vs = 0, len(virus) # 다시 초기화

        num, vx, vy = virus.popleft()

        for i in range(4):
            next_x, next_y = vx + dx[i], vy + dy[i]
            if next_x >= N or next_x < 0 or next_y >= N or next_y < 0 or map_list[next_x][next_y]!=0: continue

            map_list[next_x][next_y] = num
            virus.append([num, next_x, next_y])
            check += 1

    return map_list[X-1][Y-1]

print(bfs(map_list))