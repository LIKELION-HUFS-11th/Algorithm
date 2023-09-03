n = int(input())
budgets = list(map(int, input().split()))
m = int(input())
result = 0

def total_budget(b):
    total = 0
    for budget in budgets:
        if budget > b:
            total += b
        else:
            total += budget
    return total

def binary_search(start, end):
    global result
    if start > end:
        return result
    mid = (start + end) // 2
    tb = total_budget(mid)
    if m > tb:
        result = mid
        return binary_search(mid+1, end)
    elif m < tb: return binary_search(start, mid-1)
    else: return mid


print(binary_search(0, max(budgets)))