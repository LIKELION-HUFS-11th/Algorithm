# import sys
# input = sys.stdin.readline

# t = int(input())

# def p_func(x):
#     if x == 1 or x == 2 or x == 3:
#         return 1
#     else:
#         return p_func(x - 3) + p_func(x - 2)
    
# for _ in range(t):
#     n = int(input())
#     print(p_func(n))

import sys
input = sys.stdin.readline

t = int(input())
p = [0 for _ in range(101)]
p[1] = 1
p[2] = 1
p[3] = 1

def p_func(x):
    if p[x]:
        return p[x]
    else:
        p[x] = p_func(x - 3) + p_func(x - 2) 
        return p[x]
    
for _ in range(t):
    n = int(input())
    print(p_func(n))
