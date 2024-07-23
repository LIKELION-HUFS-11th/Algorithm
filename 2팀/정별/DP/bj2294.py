import sys

n, k = list(map(int, sys.stdin.readline().split()))

nList = list(int(sys.stdin.readline()) for _ in range(n))
# nList.sort(reverse=True)

dp= [10001] * (k+1) 
#개수 저장. dp의 각 인덱스가 가치의 최종합이고, 해당 인덱스의 값은 그 가치를 만들어내기 위핸 최소 코인 개수
#1원짜리 코인 10000개 가능한 경우가 최댓값
dp[0] = 0

for coin in nList: #각 코인들 종류별로 돌기
    for i in range(coin, k+1): #현재 코인 가지고 dp값 갱신
        dp[i] = min(dp[i], dp[i-coin]+1) #기존 값과, 현재 값에서 가져온 코인 값 빼준 사용개수

    # print(dp[coin: k+2])

if dp[k] == 10001: #안건드림
    print(-1)
else:
    print(dp[k])

    
# 그리디로 접근하려다 중단
# cnt = 0
# for i in range(n):

#     cnt += k//nList[i] 
    
#     dp[i] = k%nList[i]
#     k %= nList[i]

# print(dp, cnt)