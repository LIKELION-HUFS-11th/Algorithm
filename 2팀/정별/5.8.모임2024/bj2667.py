from collections import deque
import sys

n = int(input())
graph = []
for i in range(n):
  graph.append(list(map(int, input())))
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []
cnt = 0
 
def bfs(xPos, yPos): #인자가 시작 지점
  count = 1
  
  q = deque()
  q.append((xPos, yPos))
  graph[xPos][yPos] = 0 #시작지점 방문했으니 0으로 바꾸는 것임
  
  while q:
    x, y = q.popleft()
    for i in range(4): #상하좌우 이동
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < n and 0 <= ny < n:
        if graph[nx][ny] == 1: #집이 있다면
          graph[nx][ny] = 0 #방문했으니 바꿔주고 큐에 집어넣기
          q.append((nx, ny))
          count += 1
          
  ans.append(count)
 
for i in range(n):
  for j in range(n):
    if graph[i][j] == 1:
      bfs(i, j)
      cnt += 1
 
ans.sort()
 
print(cnt)
for i in ans:
  print(i)