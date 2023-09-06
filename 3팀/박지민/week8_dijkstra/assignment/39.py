# 완전탐색 효율성을 생각하지 않고 모든 가짓수를 따져서 답을 구할 수 있나
# 배열을 참조할 때 runtime error가 나는지 찾기

# n = 5
# arr = [1, 5, 2, 6, 8]

# # 두 배로 해줄 원소의 위치를 i로 하는 완전탐색 진행
# ans = 0
# for i in range(n):
#     # i번지에 있는 원소를 2배로 해줌
#     arr[i] *= 2

#     # 인접한 수들간의 차이의 합 구하기
#     sum_val = 0
#     for j in range(n - 1):
#         sum_val += abs(arr[j] - arr[j + 1]) # 배열 참조할 때 끝값이 넘는 거 아니야? 생각하기
    
#     # 지금까지의 최댓값과 비교하여 갱신
#     ans = max(ans, sum_val)

#     #  i번지에 있는 원소를 되돌려줌
#     arr[i] = arr[i] // 2

# print(ans)


# 이미 후보들이 리스트에 담겨있는 경우가 아니라, 알 수 없다면
# 최대 구할 때는 sys를 써서 최대/최소의 초기값을 sys.maxsize로 설정해주기

n = int(input())
arr = list(map(int, input().split()))
#모든 사람들의 이동 거리의 합이 최소가 되도록

# 0 1 2 3 4
# 1 2 3 2 6

# i = 0 일때
# j = 1부터 시작해서 j=5 까지 -> for j in range(1, 5-i)
# i+1 - (j)
# i = 1일 대
# j = 1부터 j=4까지
# i+1 4-1 5-1
import sys

INT_MAX = sys.maxsize
ans = INT_MAX
# i번 집에서 모일 때
for i in range(n):
    # 이동거리 = 명수 * (거리)
    sum_dist = 0
    # j번 집에 있는 사람들이, i번 집으로 이동하는 거리의 합
    # 거리 = abs(j-i)
    for j in range(n):
        sum_dist += arr[j] * abs(j-i)
    ans = min(ans,sum_dist)
print(ans)