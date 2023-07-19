# n 입력
n = int(input())
# nums
nums = list(map(int, input().split()))
# plus, minus, multiple, divide
plus, minus, multiple, divide = map(int, input().split())

# 설계
import sys
# max_num, min_num
max_num, min_num = -sys.maxsize, sys.maxsize

# calc
def calc(curr_num, curr_idx, plus, minus, multiple, divide):
    # 전역 변수 선언
    global max_num, min_num

    # 종료조건
    if curr_idx == n:
        # update
        max_num = max(max_num, curr_num)
        min_num = min(min_num, curr_num)
        return 
    
    if plus > 0:
        calc(curr_num + nums[curr_idx], curr_idx+1, plus-1, minus, multiple, divide)
    if minus > 0:
        calc(curr_num - nums[curr_idx], curr_idx+1, plus, minus-1, multiple, divide)
    if multiple > 0:
        calc(curr_num * nums[curr_idx], curr_idx+1, plus, minus, multiple-1, divide)
    if divide > 0:
        calc(int(curr_num / nums[curr_idx]), curr_idx+1, plus, minus, multiple, divide-1)

# calc 호출
calc(nums[0], 1, plus, minus, multiple, divide)

# 출력
print(max_num)
print(min_num)