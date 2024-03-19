import sys

n, m = map(int,sys.stdin.readline().split())
pay = list(map(int,sys.stdin.readline().split()))

result = 0
max_result = 0
for i in range(len(pay)-m+1):
    temp_sum = result - pay[i-1] + pay[i+m-1]
    result = temp_sum

    if i == 0:
        for j in range(m):
            result += pay[j]
        max_result = result
    elif max_result < temp_sum:
        max_result = temp_sum

print(max_result)

# import sys

# n, m = map(int, sys.stdin.readline().split())
# pay = list(map(int, sys.stdin.readline().split()))

# result = 0
# # 초기 부분합 계산
# for i in range(m):
#     result += pay[i]

# max_result = result  # 최대 부분합을 저장할 변수

# # 슬라이딩 윈도우 기법을 사용하여 최대 부분합 계산
# for i in range(1, n - m + 1):
#     # 새로운 부분합 계산
#     current_sum = result - pay[i - 1] + pay[i + m - 1]
#     result = current_sum  # 현재 부분합으로 업데이트

#     # 최대 부분합 업데이트
#     if current_sum > max_result:
#         max_result = current_sum

# print(max_result)

