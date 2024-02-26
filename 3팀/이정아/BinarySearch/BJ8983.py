import sys

input = sys.stdin.readline
ans = 0

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right

m, n, l = map(int, input().split())
shooting = list(map(int, input().split()))
shooting.sort()
for _ in range(n):
    x, y = list(map(int, input().split()))
    if y <= l:
        idx = binary_search(shooting, x)
        
        dist = abs(x - shooting[idx]) + y
        dist_r = abs(x - shooting[idx+1]) + y if idx < m-1 else float('inf')
        
        dist = min(dist, dist_r)
        
        if dist <= l:
            ans += 1

print(ans)
        



