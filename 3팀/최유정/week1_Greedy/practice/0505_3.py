# 숫자 카드 게임

# N : 행의 개수, M : 열의 개수
N, M = map(int, input().split())
card_list = [
    list(map(int, input().split()))
    for _ in range(N)
]
max_num = 0

for i in range(N):
    max_num = max(max_num, min(card_list[i]))

print(max_num)