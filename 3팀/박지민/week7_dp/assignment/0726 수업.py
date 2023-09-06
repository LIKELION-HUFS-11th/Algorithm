# (x,y) 칸에 대해서
#인접한 칸에 숫자 1이 3개 이상 있는지 확인
# for x in range(n):
#     for y in range(n):
#         # 어느 방향인지 몰라도 상관 없기 때문에(시계 방향 생각 안 해도 됨)
#         dxs, dys = [1,-1,0,0,], [0,0,1,-1]

#         for dx, dy in zip(dxs,dys):
#             nx,ny = x+dy, y+dy

#             cnt=0
#             for dx,dy in zip(dxs,dys):


# 
x, y = 1,2 #현재 위치
dir_num = 2 #북쪽

dxs, dys = [0,1,-1,0], [1,0,0,-1]


def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n

while keep_moving():
    nx, ny = x+dxs[dir_num], y+dys[dir_num]
    # 격차를 벗어났을 때 벽에 부딪치면
    if not in_range(nx,ny):
        dir_num = 3 - dir_num #현재 방향을 3에서 빼주면 됨
    x, y = x+ dxs[dir_num], y+ dys[dir_num]

