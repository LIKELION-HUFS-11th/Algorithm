import sys
input = sys.stdin.readline
import math

def is_prime(x:int):
    maxnum = int(math.sqrt(x))
    for i in range(maxnum, 1, -1):
        if x % i == 0:
            return False
    return True

primes = []
for x in range(2, 1000000):
    if is_prime(x):
        primes.append(x)

print(primes)

# n = int(input().rstrip())
# for _ in range(n):
#     tc = int(input().rstrip())
#     ans = 0

#     for i in range(2, tc//2+1):
#         if i in primes and tc-i in primes:
#             ans += 1
#     print(ans)
