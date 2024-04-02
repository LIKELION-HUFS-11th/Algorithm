import sys

#풀이1. 반례 못찾겠음.
N, L = map(int, sys.stdin.readline().split())

cnt = 0

ans = 0
while L<=100:
    cnt=0
    for i in range(1,L):
        cnt += i
    if (N-cnt) % L == 0:
        if L<=100:
            ans = (N-cnt) // L
            for _ in range(L):
                print(ans, end=' ')
                ans+=1
        else:
            print(-1)
            ans+=1
        break
    
    # j+=1
    L+=1

if not ans:
    print(-1)


#풀이2. 등차수열의합 활용
N, L = map(int, input().split())


# N= a + (a+1) + (a+2) +...+ (a+(L-1))
#2N= L(2a+L-1)

#a = (2N-L**2+L)/2L
#여기서 a는 0또는 자연수임. 따라서 분모분자가 나눠떨어져야 a가 나옴.

for l in range(L, 101):

    if (2*N + l - l**2) % (2*l) == 0:
        a = (2*N + l - l**2) // (2*l)
        
        if a >= 0: #a가 0또는 자연수 충족한다면.
            for i in range(a, a+l):
                print(i, end=' ')
            break
else:
    print(-1)