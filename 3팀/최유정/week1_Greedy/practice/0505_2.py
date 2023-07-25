# 큰 수의 법칙

# N : 배열의 크기, M : 숫자가 더해지는 횟수, K : 최대 연속의 수
N, M, K = map(int, input().split())
list_num = list(map(int, input().split()))
list_num.sort(reverse=True)

result = 0
cnt = 0

for _ in range(M):
    if cnt == K:
        result += list_num[1]
        cnt = 0
    else:
        result += list_num[0]
        cnt += 1

print(result)