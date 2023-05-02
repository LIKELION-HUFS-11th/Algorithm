# n, m 입력
n, m = map(int, input().split())
ball_list = list(map(int, input().split()))

# 설계
# weight_list
weight_list = [
    0 for _ in range(10)
]

# ball_list를 돌며
for ball in ball_list:
    # 같은 무게의 공 갯수 추가
    weight_list[ball-1] += 1

# ans
ans = 0

for i in range(10):
    
    # curr_comb
    curr_comb = weight_list[i] * sum(weight_list[i+1:])
    
    # ans에 curr_comb 추가
    ans += curr_comb

# 출력
print(ans)