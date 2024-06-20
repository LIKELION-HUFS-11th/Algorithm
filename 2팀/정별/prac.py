#정수로 나눠떨어져도 끝까지 다 출력. 뒤에 0000나올 수 있게.
import sys

sList =[]

lines = sys.stdin.readlines()
# print(lines)
for line in lines:
    sElem = line
    # print('g',sElem)
    sList.append(sElem)

# while True:
#     try:
#         sElem = input()
#         # if not sElem:
#         #     break
#         sList.append(sElem)
#     except EOFError:
#         break

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

        else:#큐 안에 들어있는데, 지금 돌고 있는 문자랑 다르다면
            nDict[nElem] = float(round(cnt/nSum*100, 4)) #할당
            if idx == len(sList)-1:
                nDict[elem] = float(round(cnt/nSum*100, 4))
                break
            cnt =1 #cnt 초기화
            nQue = nQue[-1:] #큐 초기화

    # while nQue:
# print(nDict)

for a in nDict.items():
    print(a[0].rstrip(), a[1])