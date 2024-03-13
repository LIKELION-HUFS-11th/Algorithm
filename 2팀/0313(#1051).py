import sys
input = sys.stdin.readline

n, m = map(int, input().split())

rec = [[0] * (m) for _ in range(n)] 

for i in range(n):
    nums = input()
    for j in range(m):
        rec[i][j] = nums[j]

space = 1

for i in range(n):
    for j in range(m):
        left = rec[i][j]
        for k in range(i + 1, n):
            for l in range(j + 1, m):
                if (k - i) == (l - j) and rec[k][l] == left and rec[i][l] == left and rec[k][j] == left:
                    space = max(space, (k - i + 1)**2)

print(space)