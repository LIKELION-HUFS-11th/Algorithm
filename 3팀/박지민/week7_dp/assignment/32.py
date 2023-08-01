#입력
# 크기 = n -> 삼각형 n x n
n = int(input())

#정수삼각형 2차원배열
triangle = [
    list(map(int, input().split()))
    for _ in range(n)
]


# d = 현재 위치까지의 최대값을 저장하는 삼각형
d = [
    [0] * n
    for _ in range(n)
]PendingDeprecationWarning

d[0][0] = triangle[0][0]


# for row in range(1,n):
#     for col in range(1,n):                
#         left_sum = triangle[row][col] + d[row-1][col-1]
#         right_sum = triangle[row][col] + d[row-1][col]

#         d[row][col] = max(left_sum, right_sum)

for i in range(0, len(triangle) - 1):
    for j in range(len(triangle[i])):
        d[i + 1][j] = max(d[i + 1][j], d[i][j] + triangle[i + 1][j])
        d[i + 1][j + 1] = max(d[i + 1][j + 1], d[i][j] + triangle[i + 1][j + 1])


#출력 : 최대합

max_val = max(d[n-1])
print(max_val)
