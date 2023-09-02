# 곱하기 혹은 더하기

from collections import deque

S = input()
s_list = deque(map(int, S))
first = s_list.popleft()
if first == 0: result = s_list.popleft()
else: result = first

while s_list:
    s = s_list.popleft()
    if s == 0: result += s
    else: result *= s

print(result)
