import sys

sosu_list =[]
M, N = map(int,sys.stdin.readline().split())

for i in range(M,N+1):
    satisfied = True
    if i == 0 or i==1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            satisfied= False
            break
    if satisfied ==True: print(i)
    

