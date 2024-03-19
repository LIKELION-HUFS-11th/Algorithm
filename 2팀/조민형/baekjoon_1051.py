import sys

N, M = map(int, sys.stdin.readline().split())
square = [[0] * M for _ in range(N)]
max_square = min(N,M)
for i in range(N):
    horizontal = sys.stdin.readline()
    for j in range(M):
        square[i][j] = int(horizontal[j])

for l in range(max_square, 0, -1):
    for x in range(len(square)-l+1):
        for y in range(len(square[0])-l+1):
            if square[x][y] == square[x+l-1][y+l-1] == square[x+l-1][y] == square[x][y+l-1]:
                print(l**2)
                exit()
        