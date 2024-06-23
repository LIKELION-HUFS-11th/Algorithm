#정수로 나눠떨어져도 끝까지 다 출력. 뒤에 0000나올 수 있게.
#뒤에 오답 풀이 있음
import sys
from collections import defaultdict

input = sys.stdin.read #이게 한꺼번에 싹읽는것임
sList = input().splitlines() #입력을 한 번에 읽고 줄 단위로 나눔.

nDict = defaultdict(int)
nSum = len(sList) #총 문자들의 수

for tree in sList:
    nDict[tree] +=1

sorted_species = sorted(nDict.items())

for species, cnt in sorted_species:
    percentage = (cnt /nSum) *100
    print(f"{species} {percentage:.4f}")

#오답풀이
#틀린부분0 코드가 너무 번잡함. cnt도 처음부터 1씩 일괄부여 가능.
import sys

sList =[]
lines = sys.stdin.readlines()
#틀린부분1
#lines에 'Oak\n', 'Pine\n', 'Pine\n', 'Maple\n',,]
#이런식으로 담김. 즉! 맨 마지막 애는 뒤에 \n이 없으니까 다른 놈으로 취급됨

for line in lines:
    sElem = line
    # print('g',sElem)
    sList.append(sElem)

sList = sorted(sList)
nSum = len(sList) #총 문자들의 수
# print(sList)
nQue =[]
cnt =0 #각 문자별 나온 절대적 횟수
nDict ={}

for idx, elem in enumerate(sList):
    nQue.append(elem)
    if nQue:
        nElem = nQue[0] #지금 순서 전까지 큐에 들어있던 숫자
        # print(nElem)
        if elem == nElem: #지금 돌고 있는 문자랑, 큐에 있는 문자랑 같다면
            cnt+=1
            if idx == len(sList)-1:#마지막 문자가 스택에 쌓여있는 애라면
                nDict[elem] = float(round(cnt/nSum*100, 4))
#틀린부분2
#round로 하니까 앞에서 이미 나눠떨어지는 경우
    #예로 25.5 , 37.0 이렇게 나옴.
#근데 무조건 뒤에 0000을 붙여서라도 4자리수 만들어야함.
#그래서 round가 아니라 f string을 써야함.

        else:#큐 안에 들어있는데, 지금 돌고 있는 문자랑 다르다면
            nDict[nElem] = float(round(cnt/nSum*100, 4)) #할당
#틀린부분3
#가장 끝에서 2번째 나무가 nDict에서 갱신이 되었음.
    #근데 이 떄의 cnt를
    #가장 끝번째 나무가 그대로 갖고감. 즉, 무조건 1이 아닐 수 있는데도 가져가는 경우
            if idx == len(sList)-1:
                nDict[elem] = float(round(cnt/nSum*100, 4))
                break
            cnt =1 #cnt 초기화
            nQue = nQue[-1:] #큐 초기화

for a in nDict.items():
    print(a[0].rstrip(), a[1])