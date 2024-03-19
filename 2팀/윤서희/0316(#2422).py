# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())  # 아이스크림 종류 수, 먹으면 안되는 조합 수
# combis = []

# for _ in range(m):
#     combi = list(map(int, input().split()))
#     combis.append(combi)

# cnt = 0

# for i in range(1, n):
#     for j in range(i + 1, n + 1):
#         for k in range(j + 1, n + 1):
#             if [i, j] not in combis and [j, k] not in combis and [i, k] not in combis:
#                 cnt += 1

# print(cnt)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # 아이스크림 종류 수, 먹으면 안되는 조합 수
combis = [[0] * (n + 1) for _ in range(n + 1)] 

for _ in range(m):
    a, b = map(int, input().split())
    combis[a][b] = 1
    combis[b][a] = 1

cnt = 0

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        for k in range(j + 1, n + 1):
            if combis[i][j] == 0 and combis[j][k] == 0 and combis[k][i] == 0:
                cnt += 1

print(cnt)