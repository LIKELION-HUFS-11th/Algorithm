import sys

n = int(input())
nList = list(map(int, sys.stdin.readline().split()))
s = int(input())

for i in range(n):#i가 포인터임
    
    nRange = i+s+1
    nMax = max(nList[i: min(n, nRange)]) #최대 교환횟수까지 고려해서 앞으로 빼야할 최댓값 찾기
    idx = nList.index(nMax) #최댓값 인덱스 저장
    
    for j in range(idx, i, -1): #거꾸로 내려가면서, 붙어있는 요소들 교체
        nList[j], nList[j-1] = nList[j-1], nList[j]
    
    s-= idx-i #최댓값 위치에서 현재 위치까지 이동한만큼 횟수임
    if s<=0:
        break #종료조건
    
print(*nList)
        

# 한번 바뀐게 계속 바뀔 수 있다는걸 간과함
# n = int(input())
# nList = list(map(int, sys.stdin.readline().split()))
# nList.append(0)

# s = int(input())
# # print(nList)
# nAns = [] #정답 리스트

# nPnt = 0
# if not s:
#     nAns = nList[:-1]
# else:
#     while s>0:
#         if nList[nPnt] == 0:
#             break
#         if nList[nPnt] < nList[nPnt+1]:
#             nAns.append(nList[nPnt+1])
#             nAns.append(nList[nPnt])
            
#             nPnt+=2
#         else:
#             nPnt+=1
#         s-=1
#     if len(nAns) != len(nList)-1:
#         for elem in nList[nPnt:n]:
#             nAns.append(elem)
#     # nAns.append(nList[nPnt+1:n])

# # print(*nAns)