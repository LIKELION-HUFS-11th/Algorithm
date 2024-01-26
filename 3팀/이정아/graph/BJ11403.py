import sys

n = int(input())
arr = list(list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = 1

for row in arr:
    print(*row)