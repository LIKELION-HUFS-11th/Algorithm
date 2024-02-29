import sys

N = int(sys.stdin.readline())

if N == 1: print(1)
elif N == 2: print(2)
elif N>=3:
    print(N + (N-2))