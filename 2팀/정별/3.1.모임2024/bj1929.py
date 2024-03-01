#700ms
import sys
m, n = map(int, sys.stdin.readline().split())

# for i in range(m, n+1):
    
#     flag = 0
#     for j in range(2, i):
#         if i % j == 0: #합성수면
#             flag +=1
#             break
#     if flag >0:
#         continue
#     print(i)

nAr = [0] * (n+1)

for i, elem in enumerate(nAr):

    if elem or i == 0 or i == 1: #elem이 1이상이면
        continue #다음 i로 넘어감
    for j in range(1, n//i +1):
        if j == 1:
            continue
        nAr[i * j] +=1

for i, elem in enumerate(nAr):
    if i< m or i == 1:
        continue
    if not elem: #elem이 0인 애들
        print(i)
    