class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x,y):
            #조건 : 바깥으로 나가면 안됨
            if y < 0 or y >= len(grid[0]) or x<0 or x>= len(grid) or grid[x][y] != '1':
                return
            
            #방문한 곳을 0으로 바꾸어 중복 방지
            grid[x][y] = 0

            #계속해서 탐색하면서 이어져있는 육지 찾기
            dfs(x-1,y) 
            dfs(x,y-1)
            dfs(x+1,y)
            dfs(x,y+1)

        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == '1':
                    dfs(x,y)
                    count += 1

        return count