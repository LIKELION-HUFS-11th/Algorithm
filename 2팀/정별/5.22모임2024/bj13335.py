import sys

q=[]
N,W,L=map(int,input().split()) 
truck= list(map(int, sys.stdin.readline().split()))
cnt=0

while truck:
    if len(q) >= W:
        del q[0]
        
    if truck:
        tmp = truck[0]
        del truck[0]
        if tmp + sum(q) <= L:
            q.append(tmp)
        else:
            q.append(0)
            truck=[tmp] + truck
    cnt+=1
if sum(q)>0:
    q=q+[0 for _ in range(W-len(q))]
        
    while q:
        q.pop()
        cnt+=1
        
print(cnt)


