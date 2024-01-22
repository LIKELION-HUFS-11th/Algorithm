m, n = map(int, input().split())
grid = [
    list(input())
    for _ in range(n)
]
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x, y):
        return False
    
    if grid[x][y] == '1':
        return False
    
    return True

start_x, start_y = 0, 0
def dfs(x, y):
    global start_x, start_y
    dxs, dys = [1, 0], [0, 1]
    for i in range(2):
        nx = x + dxs[i]
        ny = y + dys[i]
        if can_go(nx, ny):
            dfs(nx, ny)

    if start_x != 0:
        start_x, start_y = x, y

dfs(0, 0)
print(start_x, start_y)


'''
1. 오른쪽, 아래 둘 다 막혀 있으면 heap에 (좌표, 지금까지 뿌신 개수) 추가
2. heap에서 하나씩 빼면서 최대한 갈 수 있는 곳까지 
'''