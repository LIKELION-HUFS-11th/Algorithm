grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
class Solution:
    def numIslands(self, grid: List[List[str]]):
        cnt = 0

        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'  # 방문한 노드를 '0'으로 표시
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)

        for i in range(len(grid)):  # 행
            for j in range(len(grid[i])):  # 열
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    cnt += 1  
        return cnt
    
    

# for i, j in enumerate(grid):
#     if j == '1':
#         cnt += 1
        
#     print(i, j)

# def dfs(self, grid, i, j):
#     if i <0 | i >= 0 | len(grid) | j <0 | j >= len(grid[0]) | grid[i][j] == '0':
#         return

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if [i][j] == '1':
#             dfs(self, grid, i-1, j)
#             dfs(self, grid, i+1, j)
#             dfs(self, grid, i, j-1)
#             dfs(self, grid, i, j+1)
            
                