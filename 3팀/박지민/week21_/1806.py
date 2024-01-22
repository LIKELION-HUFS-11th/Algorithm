## 아이디어
# 10개 짜리 수열이 주어지는데 연속된 것들의 합 중에서 15이상이 되는 애들을 찾고
# 그 중 가장 짧은 애를 구해서
# 걔의 길이를 반환해라

## 변수
n, s = map(int, input().split())
data = list(map(int, input().split()))

min_length = float('inf')
interval_sum = 0
start = 0

for end in range(n):
    interval_sum += data[end]
    # if가 아닌 while로 해야 같은 end에 대한 진짜 최소 길이를 구할 수 있음
    while interval_sum >= s: 
        min_length = min(min_length, end - start + 1)
        interval_sum -= data[start]
        start += 1

if min_length == float('inf'):
    print(0)
else:
    print(min_length)

## 투 포인터 알고리즘
# ## 특정 합을 갖는 부분 연속 수열 찾기
# n = 5 # 현재 원소의 개수
# m = 5 # 찾고자 하는 부분합

# interval_sum = 0
# count = 0
# end = 0

# data = list(map(int, input().split()))

# ## start를 하나씩 증가시키며 반복
# for start in range(n):
#     # 부분합이 m보다 작다면 
#     while interval_sum < m and end < n:
#         interval_sum += data[end]
#         end += 1
#     if interval_sum == m:
#         count += 1
#         # 다음 start 위치를 탐색하려면 이전 start의 값은 부분합에서 빼줘야 함
#     interval_sum = interval_sum - data[start]

# print(count)
    

