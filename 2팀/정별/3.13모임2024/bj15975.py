import sys
n = int(input())
dict ={}

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dict[x] =y

print(dict)