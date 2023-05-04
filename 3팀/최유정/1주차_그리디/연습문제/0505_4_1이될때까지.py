# 1. N에서 1을 뺀다, 2. N을 K로 나눈다.
N, K = map(int, input().split())
result = 0

while N != 1:
    if N < K:
        result += N
        break
    if N % K == 0:
        N //= K
    else:
        N -= 1
    result += 1

print(result)
