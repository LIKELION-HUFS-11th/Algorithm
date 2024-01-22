import sys
sys.setrecursionlimit(10001)

n = int(sys.stdin.readline())
schedule = []
max_end = 0
time = [0]
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    schedule.append((s, e))
    if e > max_end: max_end = e

schedule.sort(key=lambda x: x[1])

print(max(time))