import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 총 일수, 인출 횟수
costs = []
for _ in range(n): # 날마다 사용하는 금액 저장
    cost = int(input())
    costs.append(cost)

start = min(costs) # 가능한 가장 작은 값
end = sum(costs) # 가능한 가장 큰 값

while start <= end:
    mid = (start + end) // 2 # 중간값으로 인출금액 초기화
    money = mid
    cnt = 1 # 인출 횟수 초깃값 1

    # 각 날에 이용할 금액 순회하며 인출 횟수 세기
    for i in costs:
        if money - i < 0: 
            money = mid 
            cnt += 1
        money -= i 

    # 출금 횟수가 m 초과거나, mid 값이 하루 사용하는 최대 금액보다 작다면
    # start 갱신하여 인출 금액 늘리기
    if cnt > m or mid < max(costs):
        start = mid + 1 

    # 그렇지 않다면 end 갱신하여 인출 금액 줄이기
    else: 
        end = mid - 1 
        ans = mid # ans 갱신

print(ans)
