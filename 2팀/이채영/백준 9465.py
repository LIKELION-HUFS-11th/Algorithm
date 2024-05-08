import sys
input = sys.stdin.readline

"""
dp
...cards[0][i-2] / cards[0][i-1] / cards[0][i]
...cards[1][i-2] / cards[1][i-1] / cards[1][i]

DP[i][j] = i열 j행 스티커를 마지막으로 골랐을 때의 최대 가지
DP[0][i]의 직전cases
1) cards[1][i-1] -> cards[0][i]
2) cards[1][i-2] -> cards[0][i]

* cards[0][i-2] -> cards[0][i]는 고려하지 않는 이유 
: 반드시 cards[1][i-1]을 거쳐 가는 것이 더 이득이기 때문에 case 1과 동일한 케이스임

따라서
DP[0][i] = max(DP[1][i-2], DP[1][i-1]) + cards[0][i]
DP[1][i]도 마찬가지


"""

def max_point(cards):
    DP = [[0 for _ in range(n)] for _ in range(2)]

    # 초기화 : 1번째 열
    DP[0][0] = cards[0][0]
    DP[1][0] = cards[1][0]
    if n == 1:
        return max(DP[0][0], DP[1][0])

    # 초기화 : 2번째 열
    DP[0][1] = cards[1][0] + cards[0][1]
    DP[1][1] = cards[0][0] + cards[1][1]
    if n == 2:
        return max(DP[0][1], DP[1][1])

    for i in range(2, n):
        DP[0][i] = max(DP[1][i-2], DP[1][i-1]) + cards[0][i]
        DP[1][i] = max(DP[0][i-2], DP[0][i-1]) + cards[1][i]

    return max(DP[0][-1], DP[1][-1])



t = int(input().strip())

results = []
for _ in range(t):
    cards = [] # n*2리스트
    n = int(input().strip())

    for _ in range(2):
        cards.append(list(map(int, input().split())))

    result = max_point(cards)

    results.append(result)

for elem in results:
    print(elem)