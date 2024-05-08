# 정수 상한액 < 요청 -> 상한액으로.
# 최대합으로.
# 높은 것 순으로 상한액 처리.
# 110 -> 120 -> 140 -> 150
# 1. 150만 상한액 -> 110 120 140 = 470 -> x상한액이 나머지보다 높아야 함.
# 2. 140 150 상한액 -> 110 120 = 230 -> 255 

import sys
input = sys.stdin.readline

n = int(input().strip())
request = list(map(int, input().split()))
budget = int(input().strip())

request.sort(reverse=True) #예산 높은 순대로 적용

if sum(request) <= budget:
    print(request[0])

else:
    # target = 0 #상한액 대상 예산들
    not_target = sum(request) #상한액에 포함되지 않는 예산 총액
    for i in range(0, len(request)):
        # target += request[i]
        not_target -= request[i]

        upper = (budget - not_target) // (i + 1) #상한액
        
        satisfied = True
        for j in range(i+1, len(request)):
            if upper < request[j]:
                satisfied = False
                break #상한액 불가

        if satisfied:
            print(upper)
            break


"""
이분탐색

150 140 120 110
상한액 = 이분의 기준?
for i in range():


"""