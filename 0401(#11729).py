import sys
input = sys.stdin.readline

n = int(input())

def top(n, start, end):
    if n == 1:
        print(start, end)
    else:
        top(n - 1, start, 6 - start - end)
        print(start, end)
        top(n - 1, 6 - start - end, end)

print(2**n - 1)
top(n, 1, 3)

