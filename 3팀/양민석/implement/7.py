# 입력
n = input()

# 함수들
def is_lucky(s):
    
    # 가운데 인덱스
    mid = len(s) // 2

    # left, right
    left, right = s[:mid], s[mid:]
    
    # left_sum, right_sum
    left_sum, right_sum = 0, 0

    for i in range(len(left)):
        left_sum += int(left[i])
        right_sum += int(right[i])

    return left_sum == right_sum

# 설계
if is_lucky(n):
    print('LUCKY')
else:
    print('READY')