import sys

n = int(input())
nList = list(map(int, sys.stdin.readline().split()))

nAns = [0] * n
nStack =[]

for i in range(n):
    
    while nStack and nList[nStack[-1]] <= nList[i]: #이 조건때문에 최근으로부터 가장 큰수가 스택에 남아있는 것임
        nStack.pop()

    if nStack:
        nAns[i] =nStack[-1]+1
    
    nStack.append(i) #인덱스를 담는게 핵심ㅇㅇ

#아래는 시간초과.
# for i in range(1, n):
    
#     # if not nAns[i]:
#         j = i
#         while j>0:
            
#             if nList[i]< nList[j]:
#                 nAns[i] =j+1
#                 break
#             j-=1

print(" ".join(map(str, nAns)))