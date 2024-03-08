import sys
import math

X,Y = list(map(int,sys.stdin.readline().split()))
Z = int(Y/X*100)

if Z>98:
    print(-1)
else: print(math.ceil(((Z+1)*X - 100*Y) / (99-Z)))


# import sys
# X,Y = list(map(int,sys.stdin.readline().split()))
# Z = (Y*100)//X
# if Z >= 99:
#     print(-1)
# else:
#     start = 0
#     end = X
#     while start < end:
#         mid = (start + end) // 2
#         new_z = (Y + mid)*100 // (X + mid)
#         if new_z != Z:
#             end = mid
#         else: start = mid+1
#     mid = (start+end)//2
#     print(mid)