import math, sys

x,y = map(int, sys.stdin.readline().split())

z = (y*100)//x

r = x
l = 0
ans = x

if z>= 99:
    print(-1)
else:
    while l<=r:
        mid = (l+r)//2
        if (100* (y+mid)) //(x+mid)>z:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)


# 순차적으로 탐색했으나 시간초과
# x,y = map(int, sys.stdin.readline().split())


# z = math.floor(y/x*100)

# if z> = 99:
#     print(-1)
# else:
#     cnt = 0
#     n_x = x #처음 x값
#     while y <= n_x:
#         x +=1 
#         y +=1
#         cnt +=1
#         n_z = math.floor(y/x*100) 
#         if n_z != z:
#             print(cnt)
#             break
#     if y == n_x: #while문 다 돈것임
#         print(-1)


