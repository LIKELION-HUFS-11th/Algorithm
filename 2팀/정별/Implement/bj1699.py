import math
N = int(input())
nMin = 0

n_root =int(math.sqrt(n))

for i in range(2, n_root+1):
    n =N
    nEach = 0
    
    while n>=4:
        n -= n_root ** 2
        nEach+=1

ans+=n
print(ans)

# print(316**2)