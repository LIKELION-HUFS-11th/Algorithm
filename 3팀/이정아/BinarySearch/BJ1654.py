import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lan = []
len_sum = 0
for _ in range(k):
    l = int(input())
    lan.append(l)
    len_sum += l

maxnum = len_sum // n

def binary_search(num, target):
    if num == 1:
        return 1
    left, right = 0, num
    while left <= right:
        mid = (left+right) // 2
        cnt = 0
        for l in lan:
            cnt += l // mid
        if cnt >= target:
            left = mid + 1
        else:
            right = mid - 1
    return right

print(binary_search(maxnum, n))
            
        
    

