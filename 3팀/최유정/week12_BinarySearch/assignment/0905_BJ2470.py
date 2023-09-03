import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
x, y = float('inf'), float('inf')

def search(start, end):
    global x, y
    if start >= end:
        return [x, y]
    ss = solutions[start] + solutions[end]
    if ss == 0:
        x, y = solutions[start], solutions[end]
        return [x, y]
    if abs(ss) < abs(x+y):
        x, y = solutions[start], solutions[end]
    if ss > 0:
        return search(start, end-1)
    else:
        return search(start+1, end)

answer = search(0, len(solutions)-1)
print(answer[0], answer[1])