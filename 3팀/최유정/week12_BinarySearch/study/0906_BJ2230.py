import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def two_pointer(left, right):
    global result
    if left > right or right >= n:
        return result
    dif = n_list[right] - n_list[left]
    if dif < m:
        return two_pointer(left, right+1)
    elif dif > m:
        result = min(result, dif)
        return two_pointer(left+1, right)
    else:
        return dif

n, m = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))
result = float('inf')

n_list.sort()
print(two_pointer(0, 0))
