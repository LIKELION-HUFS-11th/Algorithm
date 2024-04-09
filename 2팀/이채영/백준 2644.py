# x = 부모 1 y = 자식 N

import sys
input = sys.stdin.readline

global dict

def dfs(target, c, cnt):
    global dict
    if target == c:
        return cnt
    
    if c not in dict.keys():
        return -1
    else:
        for elem in dict[c]:
            dfs(target, elem, cnt+1)

def bfs(a, b, cnt):
    global dict

    parent_a = []
    parent_b = []

    ch = a
    while ch in dict.keys():
        ch = dict[ch]
        parent_a.append(ch)

    ch = b
    while ch in dict.keys():
        ch = dict[ch]
        parent_b.append(ch)
        
    






def find_parent(parent, child):
    global dict
    if child not in dict.keys():
        return -1
    
    result = dfs(parent, dict[child], 1)

    if result == -1:
        result = bfs(a, b, 0)
    
    # for c in dict[child]:
    #     result = dfs(child, c, 1)

    #     if result != -1: #ok
    #         return result
        
    return -1

######

n = int(input().strip())

a, b = map(int, input().split())

m = int(input().strip())

dict = {}

for _ in range(m):
    parent, child = map(int, input().split())

    # if child in dict.keys():
    #     dict[child].append(parent)
    # else:
    dict[child] = parent

print(dict)


####
result = find_parent(a, b)

if result != -1:
    print("ok1", result)

else:
    result = find_parent(b, a)

    print("ok2", result)




"""
c/p  1   2   3   4
1    -   1
2
3
4
"""