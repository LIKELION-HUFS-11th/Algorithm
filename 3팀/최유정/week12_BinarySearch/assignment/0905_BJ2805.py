n, m = map(int, input().split())
trees = list(map(int, input().split()))
result = 0

def tree_length(l):
    total = 0
    for t in trees:
        if t > l:
            total += (t-l)
    return total

def binary_search(start, end):
    global result
    if start > end:
        return result
    mid = (start + end) // 2
    tl = tree_length(mid)
    if tl > m:
        result = mid
        return binary_search(mid+1, end)
    elif tl < m: return binary_search(start, mid-1)
    else: return mid

print(binary_search(0, max(trees)))