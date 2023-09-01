# n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 연속으로 더할 수 있는 횟수 (m >= k)
n, m, k = map(int, input().split())     # (아래 answer와 공유)
"""
nums = sorted(list(map(int, input().split())))
nums.sort(reverse=True)     

max_sum, cnt = 0, 0
for i in range(m):
    if cnt == k:
        max_sum += nums[1]
        cnt = 0
        continue
    max_sum += nums[0]
    cnt += 1

print(max_sum)
"""

# answer (simple)
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]    
"""
result = 0
while True:
    for i in range(k):      # 가장 큰 수를 K번 더하기
        if m == 0:          # m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1              # 더할 때마다 1씩 빼기

    if m == 0:              # m이 0이라면 반복문 탈출
        break               # 두 번째로 큰 수를 한 번 더하기
    result += second        # 더할 때마다 1씩 빼기
    m -= 1

print(result)
# Problem : M의 크기가 100억 이상 커진다면 시간 초과
"""

# answer (quicker)
# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += count * first
result += (m - count) * second

print(result)