import sys

N, L = list(map(int,sys.stdin.readline().split()))
street = [0 for _ in range(L)]
sign = {}
for _ in range(N):
    D, R, G = list(map(int,sys.stdin.readline().split()))
    street[D] = 1
    sign[D] = [R, G]

sanggeun = 0
time = 0
while sanggeun < len(street):
    if street[sanggeun] == 1 :
        while time % (sign[sanggeun][0] + sign[sanggeun][1]) < sign[sanggeun][0]:
            time +=1
    time += 1
    sanggeun +=1
print(time)