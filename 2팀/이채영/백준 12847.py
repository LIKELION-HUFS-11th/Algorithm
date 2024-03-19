import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pays = list(map(int, input().split()))

#슬라이딩윈도우
for i in range(0, n-m+1):
    if i == 0:
        total = sum(pays[i:i+m])
        max_total = total

    else:
        total += pays[i+m-1]
        total -= pays[i-1]

        max_total = max(total, max_total)

print(max_total)