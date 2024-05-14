import sys
input = sys.stdin.readline
from collections import deque

'''
a 물통 물의 양: x
b 물통 물의 양: y
c 물통 물의 양: z
'''

# 해당 (x, y) 상태가 방문 전이라면 방문 표시 후 q에 추가하기
def water(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x, y))

# q의 모든 상태 처리
# move: 이동한 물의 양
# water: 이동 후 새로운 상태 업데이트하여 큐에 추가
def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            case.append(z)
        
        # x -> y
        move = min(x, b - y)
        water(x - move, y + move)

        # x -> z
        move = min(x, c - z)
        water(x - move, y)

        # y -> x
        move = min(y, a - x)
        water(x + move, y - move)

        # z -> z
        move = min(y, c - z)
        water(x, y - move)

        # z -> x
        move = min(z, a - x)
        water(x + move, y)

        # z -> y
        move = min(z, b - y)
        water(x, y + move)


a, b, c = map(int, input().split())

q = deque()
q.append((0, 0))

# 방문 상태 기록
visited = [[0] * (b + 1) for _ in range(a + 1)]
visited[0][0] = 1

# 물통 a가 비어있을 때, c 물통의 물의 양 저장할 리스트
case = []

bfs()

case.sort()

for i in case:
    print(i, end=' ')


