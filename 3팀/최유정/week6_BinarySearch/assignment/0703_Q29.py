# 공유기 설치
# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))
house.sort()
result = 0

def binary_search(start, end):
    global result
    standard = house[0]
    if start > end:
        return result
    mid = (start + end) // 2
    cnt = 1
    for h in house:
        if h >= standard + mid:
            standard = h
            cnt += 1
    if cnt >= c:
        result = mid
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)

print(binary_search(1, house[n-1]-house[0]))