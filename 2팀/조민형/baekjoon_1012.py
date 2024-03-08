import sys

def explore(x, y):
    global bc_list
    stack = [(x, y)]
    while stack:
        cur_x, cur_y = stack.pop()
        bc_list[cur_x][cur_y] = 0
        # 상
        if cur_x > 0 and bc_list[cur_x-1][cur_y] == 1:
            stack.append((cur_x-1, cur_y))
        # 하
        if cur_x < len(bc_list)-1 and bc_list[cur_x+1][cur_y] == 1:
            stack.append((cur_x+1, cur_y))
        # 좌
        if cur_y > 0 and bc_list[cur_x][cur_y-1] == 1:
            stack.append((cur_x, cur_y-1))
        # 우
        if cur_y < len(bc_list[cur_x])-1 and bc_list[cur_x][cur_y+1] == 1:
            stack.append((cur_x, cur_y+1))

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    bc_list = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        bc_y, bc_x = map(int, sys.stdin.readline().split())
        bc_list[bc_x][bc_y] = 1
    count = 0
    for i in range(len(bc_list)):
        for j in range(len(bc_list[i])):
            if bc_list[i][j] == 1:
                count += 1
                explore(i, j)
    print(count)
