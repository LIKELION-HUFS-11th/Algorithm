import sys
input = sys.stdin.readline

x, y = map(int, input().split())

# 유클리드 호제법
def gcd(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

ans = x + y - gcd(x, y)
print(ans)