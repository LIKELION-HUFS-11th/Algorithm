import sys, math

N, M = map(int,sys.stdin.readline().split())

pick = 1
for j in range(N, N-3, -1): pick *= j
icecream_total = pick/(math.factorial(3))

bad_list = set()
for _ in range(M):
    tuple1, tuple2 = map(int,sys.stdin.readline().split())
    for i in range(1,N+1):
        if i != tuple1 and i != tuple2:
            bad_list.add(tuple(sorted((tuple1,tuple2, i))))

print(int(icecream_total - len(bad_list)))