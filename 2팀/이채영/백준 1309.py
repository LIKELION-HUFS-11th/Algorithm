import sys
input = sys.stdin.readline

n = int(input())

DP = [0 for _ in range(n+1)]

#초기화
DP[0] = 1
DP[1] = 3

for i in range(2,n+1):
    """
    case1) i-1번째 우리에 사자가 없는 경우 = DP[i-2]
        i번째 -> xx / ox / xo 가능
    case2) i-1번째 우리에 사자가 있는 경우 = DP[i-1]에서 case1을 제외 = DP[i-1] - DP[i-2]
        i번째 -> xx / ox(또는 xo) 가능

    DP[i] = (DP[i-2] * 3) + {(DP[i-1] - DP[i-2]) * 2}
    """

    DP[i] = (DP[i-2] + DP[i-1]*2) % 9901


print(DP[n])