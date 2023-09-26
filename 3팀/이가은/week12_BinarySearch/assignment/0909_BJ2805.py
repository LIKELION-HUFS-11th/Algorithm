'''
(실버2) 나무자르기
https://www.acmicpc.net/problem/2805
'''
# n: 나무의 수, m: 상근이가 집으로 가져가려고 하는 나무의 길이
n, m = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

def sum_heights(cutter):
    sum_diff = 0

    for elem in heights:
        if elem > cutter:
            sum_diff += (elem - cutter)
    
    return sum_diff

left, right = 0, heights[-1]
max_height = -1
while left <= right:
    mid = (left + right) // 2
    if sum_heights(mid) >= m:
        max_height = max(max_height, mid)
        left = mid + 1
    else:
        right = mid - 1

print(max_height)