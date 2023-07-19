# 입력
n = int(input())
fear_list = list(map(int, input().split()))

# 함수들
def is_ok(curr_group):
    
    # 비어있으면
    if not curr_group:
        # 실패
        return False
    
    # 마지막 사람이 여전히 무서우면
    if curr_group[-1] > len(curr_group):
        # 실패
        return False
    
    # 이외에는 성공
    return True

# 설계
# fear_list 정렬
fear_list.sort()

# ans_list
ans_list = [
    [] for _ in range(n)
]

# curr_idx
curr_idx = 0

# 낮은 순서로 넣기
for fear_idx in fear_list:
    # ans_list의 curr_idx의 길이
    curr_len = len(ans_list[curr_idx])

    # 현재 리스트가 비어있으면,
    if not curr_len:
        # 넣어주기
        ans_list[curr_idx].append(fear_idx)
    
    # 현재 리스트가 포화 상태면,
    elif ans_list[curr_idx][-1] == curr_len:
        # curr_idx를 올려주고
        curr_idx += 1
        # 넣어주기
        ans_list[curr_idx].append(fear_idx)
    
    # 현재 리스트가 포화 상태가 아니면,
    else:
        # 넣어주기
        ans_list[curr_idx].append(fear_idx)

# ans
ans = 0

# ans_list를 돌며
for group in ans_list:
    # 그룹을 확인하여 괜찮으면
    if is_ok(group):
        # ans에 추가
        ans += 1

# 출력
# print(ans_list)
print(ans)