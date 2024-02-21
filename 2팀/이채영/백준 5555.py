# https://www.acmicpc.net/problem/5555
from collections import deque

global result
result = 0

def count_rings(ring, find): #list[str], str
    global result

    index = 0
    # target = find[index]

    for i in range(len(ring) + len(find) - 1):
        if ring[i] == find[index]:
            index += 1

            if index > len(find) - 1:
                result += 1
                return
    
        ring.append(ring[i]) #원형큐처럼 순환시킴
    
    return




find = input()
N = int(input())

for _ in range(N):
    ring = list(input())
    count_rings(ring, find)

print(result)