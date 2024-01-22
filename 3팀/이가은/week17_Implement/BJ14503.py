n, m = map(int, input().split())
r, c, d = map(int, input().split())
grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

dx = [-1, 0, 1, 0] 
dy = [0, 1, 0, -1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

cnt = 0
def clean_dirs(r, c, d):
    global cnt

    if grid[r][c] == 0:
        grid[r][c] = 2
        cnt += 1
    
    for i in range(1, 5):
        drc = (d - i + 4) % 4 
        new_x = r + dx[drc]
        new_y = c + dy[drc]
        if in_range(new_x, new_y) and grid[new_x][new_y] == 0:
            return (new_x, new_y, d-i)

    drc = (d + 2) % 4
    new_x = r + dx[drc]
    new_y = c + dy[drc]
    if in_range(new_x, new_y):
        if grid[new_x][new_y] == 1:
            return (-1, -1, d)
        else:
            return (new_x, new_y, d)
    else:
        return (-1, -1, d)
        
def simulate(r, c, d):
    new_r, new_c, new_d = clean_dirs(r, c, d)
    if new_r == -1:
        return 
    else:
        return simulate(new_r, new_c, new_d)

simulate(r, c, d)
print(cnt)