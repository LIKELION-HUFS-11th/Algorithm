grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print(grid[3][0])
cnt = 0
# for i, j in enumerate(grid):
#     if j == '1':
#         cnt += 1
        
#     print(i, j)

def dfs(self, grid, i, j):
    if i <0 | i >= 0 len(grid) | j <0 | j >= len(grid[0]) | grid[i][j] == '0':
        return

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if [i][j] == '1':
            dfs(self, grid, i-1, j)
            dfs(self, grid, i+1, j)
            dfs(self, grid, i, j-1)
            dfs(self, grid, i, j+1)
            
                