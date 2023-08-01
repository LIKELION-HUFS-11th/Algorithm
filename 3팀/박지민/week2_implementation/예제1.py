n = int(input()) # n x n=공간 크기
x,y=1,1
plans = input().split() 

#이동 방향

dx = [0,0,-1,1]
dy = [-1,1,0,0]
direction = ['L','G','U','D']

for plan in plans:
    for i in range(len(direction)):
        if plan == direction[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간 벗어날 때
    if nx < 1 or ny <1 or nx >n or ny >n:
        continue

    x,y=nx,ny

print(x,y)
