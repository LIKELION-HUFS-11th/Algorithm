import sys
input = sys.stdin.readline
from collections import deque

n, w, l = map(int, input().split())  # 트럭 수, 다리 길이, 최대하중

trucks = list(map(int, input().split()))
trucks = deque(trucks)

bridge = [0] * w
bridge = deque(bridge)
time = 0

while bridge:
    time += 1
    bridge.popleft()
    if trucks:
        if sum(bridge) + trucks[0] <= l:
            bridge.append(trucks.popleft())
        else:
            bridge.append(0)
print(time)
