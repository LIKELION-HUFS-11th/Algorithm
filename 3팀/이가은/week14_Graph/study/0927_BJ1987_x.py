
import sys
sys.setrecursionlimit(10001)

r, c = map(int, sys.stdin.readline().split())

board = [
    list(sys.stdin.readline())
    for _ in range(r)
]


def in_range(x, y):
    return 0 <= x and x < r and 0 <= y and y < c

dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]

max_cnt, cnt = 0, 1
visited = set()

def dfs(x, y):
    global max_cnt, cnt, visited

    for i in range(4):
        nx = x + dxs[i]
        ny = y + dys[i]
        
        if in_range(nx,ny):
            if board[nx][ny] not in visited:
                visited.add(board[nx][ny])
                cnt += 1
                max_cnt = max(max_cnt, cnt)
                dfs(nx, ny)
                visited.remove(board[nx][ny])
                cnt -= 1

visited.add(board[0][0])
dfs(0, 0)
print(max_cnt)