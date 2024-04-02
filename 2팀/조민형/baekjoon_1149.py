import sys

# dp 문제 -> 2차원 배열로 만들어 풀이
n = int(sys.stdin.readline())
# 한 리스트 안에  r,g,b 요소를 지닌 리스트가 n개 입력받기
costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 맨 처음부터 마지막까지 리스트를 돌면서 자신과 다른 색깔 중에서 가장 최소값을 찾아 다음 리스트에 더함
# 누적하면서 아래로 계속 내려가면 마지막에 있는 값이 모든 집을 칠하는 비용의 최솟값
for i in range(1, n): # 그 전 최소값과 비교하여 더해야 하므로 1부터 index가 시작
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])

print(min(costs[-1]))