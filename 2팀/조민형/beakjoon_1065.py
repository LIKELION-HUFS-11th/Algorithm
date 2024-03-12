import sys

N = int(sys.stdin.readline())

def countNum(number):
    if number >= 100:
        hundred = number//100
        ten =  (number%100)// 10
        one = (number%100)%10
        if hundred - ten == ten-one:
            return True
        else: return False
    else: return True

count = 0
for i in range(1,N+1):
    if countNum(i):
        count +=1

print(count)