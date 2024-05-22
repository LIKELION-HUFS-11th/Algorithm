import sys

N=int(sys.stdin.readline())

dp_max=list(map(int,sys.stdin.readline().split()))
dp_min=dp_max
 
for i in range(1,N):
    a,b,c = map(int,sys.stdin.readline().split())
    dp_max=[a+max(dp_max[0],dp_max[1]),b+max(dp_max[0],dp_max[1],dp_max[2]),c+max(dp_max[1],dp_max[2])]
    dp_min=[a+min(dp_min[0],dp_min[1]),b+min(dp_min[0],dp_min[1],dp_min[2]),c+min(dp_min[1],dp_min[2])]
 
 
print(max(dp_max),min(dp_min))