import sys
# input = sys.stdin.readline()
# 정해진 총액 이하에서 가능한 한 최대의 총 예산
# #합이 총액 안넘으면, 지방 예산 중 가장 최댓값

# 120 110 127 127
# => 472
# 총액에서 빼면 1
#리스트에 각 지방 자리에, 첫예산 - 총액/4 위치시키기
n = int(input())
nList = list(map(int, sys.stdin.readline().split()))
nTotal = int(input())

nDiffer = [0 for _ in range(n)]
nSum = 0

for elem in nList:
    nSum += elem

if nSum<= nTotal: #지방들 요청 전부 수용 가능하다면.
    nMax=0
    for elem in nList:
        if nMax < elem:
            nMax = elem
    print(nMax)
else:
    nSum = 0
    nLine = nTotal//n
    for i, nRegion in enumerate(nList):
        if nRegion > nLine: #일단 상한선은 n빵에서 시작.
            nDiffer[i] = nRegion - nLine
            nSum += nLine
        else:
            nSum += nRegion #line 밑에 있는 애들은 다 더하기
    nTotal -= nSum

    nG = 0
    for elem in nDiffer:
        if elem: nG+=1

    nLine += nTotal // nG
    print(nLine)

    
    





