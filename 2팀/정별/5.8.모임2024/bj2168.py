# 참고 사이트: https://m.blog.naver.com/orbis1020/220664563768
import sys, math

x, y = map(int, sys.stdin.readline().split())

#최대공약수 코드. 유클리드 호제법
def gcd(x, y):
    while y > 0:
        x, y = y, x %y
    return x

print(x+y-gcd(x,y))