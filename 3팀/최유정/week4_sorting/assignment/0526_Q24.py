# 안테나
# https://www.acmicpc.net/problem/18310

import math
import sys
input = sys.stdin.readline

N = int(input())
house = list(map(int, input().split()))
house.sort()
center_num = math.ceil(N / 2)
print(house[center_num-1])