import sys

n,m,s = map(int, sys.stdin.readline().split())
nOthers = []#다른 수업일정

nTotal =[0 for _ in range(s+1)] # 총 수업일정.

for _ in range(n):
    x,y = list(map(int, sys.stdin.readline().split()))

    for i in range(x, x+y+1):
        nTotal[i] =1
# print(nTotal)   
nStart = 0 #수업시작시간. 정답임.
# def test(m,s):
#     if  :
#         return nStart   
    # return -1

flag = True
for idx, bClass in enumerate(nTotal):
    if not flag: #답구해졌으면
        break
    if bClass:
        continue #1 들어가있으면 다른 수업 있음
    else: #0이면 시작
        nStart = idx-1
        nFinish = idx
        while idx-1 + m > nFinish:
            if nTotal[nFinish]: #1존재하면
                break
            elif not nTotal[nFinish]:
                nFinish+=1

            if nFinish-idx+1 ==m:
                print(nStart)
                flag = False
                break
     
if flag:
    print(-1)
