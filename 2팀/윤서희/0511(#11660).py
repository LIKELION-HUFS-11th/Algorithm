import sys
input = sys.stdin.readline

n , m = map(int, input().split()) # 표의 크기, 구해야 하는 횟수
graph = [[0] * (n + 1)]
for _ in range(n):
    row = [0] + list(map(int, input().split()))
    graph.append(row)

# 행의 누적합
for i in range(0, n + 1):
    for j in range(0, n):
        graph[i][j + 1] += graph[i][j]

'''
[[0, 0, 0, 0],
 [1, 3, 6, 10], 
 [2, 5, 9, 14], 
 [3, 7, 12, 18], 
 [4, 9, 15, 22]]
'''

# 열의 누적합
for i in range(0, n):
    for j in range(0, n + 1):
        graph[i + 1][j] += graph[i][j]

'''
[[0, 0, 0, 0],
 [1, 3, 6, 10], 
 [3, 8, 15, 24], 
 [6, 15, 27, 42], 
 [10, 24, 42, 64]]
'''

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = graph[x2][y2] - graph[x1 - 1][y2] - graph[x2][y1 - 1] + graph[x1 - 1][y1 - 1]
    print(ans)



