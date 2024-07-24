import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
networks = []
for _ in range(n):
    networks.append(list(map(int, input().split())))

