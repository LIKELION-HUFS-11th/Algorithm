# import sys 
# input = sys.stdin.readline

# n, m = map(int, input().split())

# sets = [[0] * (n + 1) for _ in range(n + 1)] 

# for i in range(m):
#     operator, a, b = map(int, input().split())
#     if operator == 0:
#         sets[a][b] = 1
#         sets[b][a] = 1
#     elif operator == 1:
#         if sets[a][b] == 1:
#             print("YES")
#         else:
#             print("NO")

import sys
sys.setrecursionlimit(10**6) # 재귀 제한

def union(x, y):  
    x = sets(x)
    y = sets(y)
    if x == y: # 두 부모가 같지 않다면 하나의 집합으로 합치기
        return
    else:
        nums[y] = x

def sets(target): # 재귀적으로 원소의 붐 찾기
    if target == nums[target]:
        return target
    nums[target] = sets(nums[target])
    return nums[target]


n, m = map(int, sys.stdin.readline().split())
nums = [i for i in range(n + 1)]  # [1 2 3 4 5 ... n]

for _ in range(m):
    operator, a, b = map(int, sys.stdin.readline().split())
    print(nums)
    if operator == 0:
        union(a, b)
    elif operator == 1:
        if sets(a) == sets(b):
            print("YES")
        else:
            print("NO")