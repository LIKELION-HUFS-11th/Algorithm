# 입력
s = input()

# 설계
# zero_group_cnt, one_group_cnt
zero_group_cnt, one_group_cnt = 0, 0
# 첫 원소 처리
if s[0] == '0':
    zero_group_cnt += 1
else:
    one_group_cnt += 1

# s를 탐색하면서
for i in range(1, len(s)):
    # 달라지는 순간
    if s[i] != s[i-1]:
        # 바뀐 후가 1이면
        if s[i] == '1':
            one_group_cnt += 1
        # 바뀐 후가 0이면
        else:
            zero_group_cnt += 1

# 출력
print(min(one_group_cnt, zero_group_cnt))