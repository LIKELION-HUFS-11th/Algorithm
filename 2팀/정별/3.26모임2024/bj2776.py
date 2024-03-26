import sys

T = int(input())

N = int(input())
Note1 = list(map(int, sys.stdin.readline().split()))

M = int(input())
Note2 = list(map(int, sys.stdin.readline().split()))

Note1.sort()

# for elem in Note2:
#     if elem in Note1:
#         print(1)
#     else:
#         print(0)

for i in range(M):
    target = Note2[i]
    
    l = 0
    r = N-1
    result = -1 #찾고자 하는 인덱스 번호
    
    while l <= r:
        mid = (l+r)//2
        if target == Note1[mid]:
            result = mid
            break
        elif target > Note1[mid]:
            l = mid +1
        else:
            r = mid-1
    if result != -1: #바뀌었ㅇ다면
        print(1)
    else:
        print(0)

