import sys

N = int(sys.stdin.readline())
count = 0
while N != 1:
    if N % 3 == 0:
        count+=1
        N = N//3
    elif N % 3 == 1 and N>3:
        N -= 1
        count += 2
        N = N//3
    elif N % 2 == 0:
        count+=1
        N = N//2
    else:
        count+=1
        N -= 1
print(count)