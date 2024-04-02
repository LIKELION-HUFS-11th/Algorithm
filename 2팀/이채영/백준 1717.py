"""
1 3 
7 6
-
1 3 7 6
4 2
-
1 3 7 6
4 2
"""

# 메모리초과 (딕셔너리가 최대 100000개)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sets = []
dict = {}

for i in range(n+1):
    # sets.append(set(i))
    dict[i] = set([i])

for _ in range(m):
    op, a, b = map(int, input().split())

    if op == 0:
        set_union = dict[a] | dict[b]

        dict[a] = set_union
        dict[b] = set_union

    else:
        if b in dict[a]:
            print("yes")
        else:
            print("no")