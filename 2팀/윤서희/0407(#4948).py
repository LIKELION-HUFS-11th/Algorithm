# 시간초과

# import sys
# input = sys.stdin.readline

# def is_prime(x):
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return False 
#     return True 

# while True:
#     n = int(input())
#     cnt = 0
#     if n == 0:
#         break
#     for i in range(n + 1, 2 * n + 1):
#         if is_prime(i):
#             cnt += 1
#     print(cnt)


import sys
input = sys.stdin.readline

def is_prime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False 
    return True 

n = 123456
nums = [0] * (n * 2 + 1)

for i in range(n * 2 + 1):
    if is_prime(i):
        nums[i] = 1

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    for i in range(n + 1, 2 * n + 1):
        if nums[i] == 1:
            cnt += 1
    print(cnt)