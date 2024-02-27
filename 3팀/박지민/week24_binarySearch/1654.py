# 입력
already_have, needed = map(int, input().split())
already_have_list = [ int(input()) for _ in range(already_have) ]

# 이진 탐색
start, end = 1, max(already_have_list)
while start <= end:
    mid = (start + end) // 2
    line_cnt_sum = 0
    for line in already_have_list:
        line_cnt = line // mid
        line_cnt_sum += line_cnt
    if line_cnt_sum >= needed:
        start = mid + 1
    else:
        end = mid - 1
print(end)

    

# # 1. mid 값으로 각 랜선을 나눴을 때의 몫

# line_list = [802, 743, 457, 539]
# mid = 229
# line_cnt_sum = 0
# for line in line_list:
#     line_cnt = line // mid 
#     line_cnt_sum += line_cnt

# print(line_cnt_sum)


