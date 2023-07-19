# 고정점 찾기

n = int(input())
n_list = list(map(int, input().split()))

def binary_search(start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if n_list[mid] == mid:
        return mid
    elif n_list[mid] < mid:
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)

print(binary_search(0, n-1))