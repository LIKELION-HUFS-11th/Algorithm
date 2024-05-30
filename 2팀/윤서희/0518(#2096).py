import sys
input = sys.stdin.readline

n = int(input())

max_num = [0] * 3
min_num = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())

    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_num[j], max_num[j + 1])
            min_tmp[j] = a + min(min_num[j], min_num[j + 1])
        elif j == 1:
            max_tmp[j] = b + max(max_num[j - 1], max_num[j], max_num[j + 1])
            min_tmp[j] = b + min(min_num[j - 1], min_num[j], min_num[j + 1])
        else:
            max_tmp[j] = c + max(max_num[j], max_num[j - 1])
            min_tmp[j] = c + min(min_num[j], min_num[j - 1])
    
    for i in range(3):
        max_num[i] = max_tmp[i]
        min_num[i] = min_tmp[i]


print(max(max_num), min(min_num))


# import sys
# input = sys.stdin.readline

# n = int(input())
# nums = [list(map(int, input().split())) for _ in range(n)]
# max_num = [[0, 0, 0] for _ in range(n)]
# min_num = [[0, 0, 0] for _ in range(n)]
# max_num[0] = nums[0]
# min_num[0] = nums[0]

# for i in range(1, n):
#     for j in range(3):
#         if j == 0:
#             max_num[i][j] = max(max_num[i - 1][j] + nums[i][j], max_num[i - 1][j + 1] + nums[i][j]) 
#             min_num[i][j] = min(min_num[i - 1][j] + nums[i][j], min_num[i - 1][j + 1] + nums[i][j]) 
#         elif j == 1:
#             max_num[i][j] = max(max_num[i - 1][j - 1] + nums[i][j], max_num[i - 1][j] + nums[i][j], max_num[i - 1][j + 1] + nums[i][j]) 
#             min_num[i][j] = min(min_num[i - 1][j - 1] + nums[i][j], min_num[i - 1][j] + nums[i][j], min_num[i - 1][j + 1] + nums[i][j]) 
#         else:
#             max_num[i][j] = max(max_num[i - 1][j] + nums[i][j], max_num[i - 1][j - 1] + nums[i][j]) 
#             min_num[i][j] = min(min_num[i - 1][j] + nums[i][j], min_num[i - 1][j +-1] + nums[i][j]) 


# print(max(max_num[n - 1]), min(min_num[n - 1]))
