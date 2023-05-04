from itertools import combinations

# N : 볼링공의 개수, M : 공의 최대 무게
N, M = map(int, input().split())
K = list(map(int, input().split()))

cnt = 0

total = len(list(combinations(K, 2)))

for i in range(1, M+1):
    if K.count(i) > 1:
        cnt += len(list(combinations(range(K.count(i)), 2)))
total -= cnt
print(total)