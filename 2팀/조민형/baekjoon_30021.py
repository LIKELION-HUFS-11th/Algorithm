import sys

def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

N = int(sys.stdin.readline())
N_list = [i for i in range(1,N+1)]
used= [False for _ in range(N)]
count = 0 
result = []

if N == 1:
    print("YES\n1")
elif N==2:
    print("NO")
else:
    print("YES")
    fullcount = N*(N+1)//2
    j=0
    while count != fullcount:
        j += 1
        j %= len(N_list)
        if not is_prime(count + N_list[j]) and used[j] == False :
            used[j] = True
            print(N_list[j], end=" ")
            count += N_list[j]
            j=0
    