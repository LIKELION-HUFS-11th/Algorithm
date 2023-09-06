# 6 4
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# 6x4 

# 하루가 지나면 상하좌우에 있는 0인 토마토들은 1로 변함
# 익은 애들의 상하좌우를 체크하면서
# day[i][j] ==0인  i행j열 위치의 토마토가 익었는지

from collections import deque;

## 입력
n,m = tuple(map(int, input().split()))
# 최소 일수를 
day = [
    [0] * m
    for _ in range(n)
]
# box에 토마토 정보(익:1, 안익: 0, 없: -1)넣고
box = []

deq = deque()
for j in range(n):
    box.append([int(x) for x in input().split()])
    # 익은 토마토는 deq에 저장
    for i in range(m):
        if box[i][j] == 1:
            deq.append([i,j])

##

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# 범위 안에 있는지 확인하는 함수
def in_range(x,y):
    return 0<=x and x<m and 0<=y and y<n

count = 0
while deque:
    x, y = deq.popleft()
    for _ in range(4):
        nx = x + dx
        ny = y + dy
        #범위 안에 있고 안 익었다면
        if in_range(nx, ny) and box[nx][ny] == 0:
            # 익은 토마토로 바뀔 꺼고
            box[nx][ny] = 1
        # 하루 지난 거 표시
        day[x][y] += 1


## 출력

# 최소 일수: box를 모두 돌면서 값이 모두 1이면 -> 그 때 day에 있는 1의 개수 출력

# 
# 최소 일수 출력하는 함수
ans = 0
def min_days():
    for j in range(n):
        for i in range(m):
            if day[i][j] != 0:
                ans += 1
    return ans

## 모두 돌면서 모두 1이면
cnt = 0
for j in range(n):
    for i in range(m):
        if box[i][j] == 1:
            cnt += 1
        elif cnt == m*n:
            print(min_days)



 ## box[i][j] : 토마토
# i\j 0 1 2 3 4 5
#  0   
#  1
#  2
#  3

 ## day[i][j] : 최소 일수
#  0 1 2 3 4 5
# 0 
# 1
# 2
# 3

# # 0일          
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1

# # 1일
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 0 0 0 0 1 1

# # 2일
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 0 0 0 0 1 1
# 0 0 0 1 1 1

# # 3일
# 0 0 0 0 0 0
# 0 0 0 0 0 1
# 0 0 0 0 1 1
# 0 0 0 1 1 1

# # 4일





