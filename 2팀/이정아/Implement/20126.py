import sys
input = sys.stdin.readline

n, m, s = map(int, input().split())
times = []
for _ in range(n):
    x, y = map(int, input().split())
    start, end = x, x+y
    times.append([start, end])
times.sort()

def solve():
    # 강의실 빌리는 시작 시간부터 m시까지 비어있다면 0
    if times[0][0] >= m:
        return 0
    for i in range(len(times)-1):
        # 다른 시험 사이의 비는 시간이 m 이상이라면 앞의 시험 끝나자마자 바로
        if (times[i+1][0] - times[i][1]) >= m:
            return times[i][1]
    # 마지막 다른 시험이 끝난 시점부터 s시까지의 시간이 m 이상이라면 마지막 시험 끝나자마자 바로
    if (s - times[-1][1]) >= m:
        return times[-1][1]
    return -1

print(solve())

