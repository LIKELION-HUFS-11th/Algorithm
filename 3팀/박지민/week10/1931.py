import sys

n = int(sys.stdin.readline()) #회의의 수
times = []
for _ in range(n):
    start, end= sys.stdin.readline().rstrip()
    times.append([start,end])


