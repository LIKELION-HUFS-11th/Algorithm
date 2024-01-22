'''
(실버2) 예산
https://www.acmicpc.net/problem/2512
'''
n = int(input())                            # n: 지방의 수  
requests = list(map(int, input().split()))  # requests: 예산 요청액 리스트
budget = int(input())                       # budget: 예산
requests.sort()

def calc_requests(limit):
    sum_requests = 0
    for elem in requests:
        if elem <= limit:
            sum_requests += elem
        else:
            sum_requests += limit
    
    return sum_requests
    
left, right = 0, requests[-1]
max_limit = -1
while left <= right:
    mid = (left + right) // 2
    if calc_requests(mid) <= budget:
        max_limit = max(max_limit, mid)
        right = mid - 1
    else:
        left = mid + 1

print(max_limit) 