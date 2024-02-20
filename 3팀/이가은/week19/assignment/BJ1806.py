import sys
sys.setrecursionlimit(10001)

n, s = map(int, input().split())
nums = list(map(int, input().split()))
min_len = 100000

for i in range(n-1): # i = 0~n-2
    length = 1
    sum = nums[i]
    if sum >= s:
        min_len = 1
        break

    for j in range(i, n, 1):    # j = i~n-1
        sum += nums[j]
        length += 1
        if sum >= s:
            min_len = min(length, min_len)
            break

if min_len == 10000:
    print(0)
else:
    print(min_len)

