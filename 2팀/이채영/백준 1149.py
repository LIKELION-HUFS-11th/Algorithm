import sys
input = sys.stdin.readline

#양쪽의 집들과 서로 색이 달라야 함.
#얘도 DP네... n*3 리스트
"""
    0   1   2
0   0   0   0
1   26  40  83   
2   
3
4
..
N-1
N
"""

n = int(input().strip())

DP = [[0 for _ in range(3)] for _ in range(n + 1)]
fee = [[0, 0, 0]]

for _ in range(n):
    fee.append(list(map(int, input().split())))

DP[1] = fee[1]

for i in range(2, n+1):
    #i번째 집에 0번 페인트를 칠함 <= i-1번째 집엔 1 Or 2번 페인트를 칠함
    DP[i][0] = fee[i][0] + min(DP[i-1][1], DP[i-1][2])
    DP[i][1] = fee[i][1] + min(DP[i-1][0], DP[i-1][2])
    DP[i][2] = fee[i][2] + min(DP[i-1][0], DP[i-1][1])

print(min(DP[n]))