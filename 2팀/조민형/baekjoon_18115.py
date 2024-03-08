import sys
from collections import deque
        
N = int(sys.stdin.readline())
trick_list = list(map(int,sys.stdin.readline().split()))
trick_list.reverse()

dq = deque()
for j in range(N):
    if trick_list[j] == 1:
        dq.appendleft(j+1)
    elif trick_list[j] == 2:
        dq.insert(1,j+1)
    elif trick_list[j] == 3:
        dq.append(j+1)
    N-=1

for i in dq:
    print(i, end=" ")