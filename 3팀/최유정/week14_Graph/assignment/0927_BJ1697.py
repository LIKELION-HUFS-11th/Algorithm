from collections import deque

# x+1, x-1, x*2

N, K = map(int, input().split())
x_list = [0] * 100001
q = deque([N])

while q:
    s = q.popleft()
    if s == K:
        print(x_list[s])
        break
    for ns in [s-1, s+1, s*2]:
        if 0 <= ns <= 100000 and x_list[ns] == 0:
            x_list[ns] = x_list[s] + 1
            q.append(ns)
