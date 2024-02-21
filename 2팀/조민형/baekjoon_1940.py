import sys

N = int(sys.stdin.readline().rstrip('\n'))
M = int(sys.stdin.readline().rstrip('\n'))

armorList = list(map(int,sys.stdin.readline().split()))
alreadyUsed = []
result = 0

armorList.sort()

left=0
right=len(armorList)-1
while left<right:
    if armorList[left] + armorList[right] == M:
        result += 1
        left+=1
        right-=1
    elif armorList[left] + armorList[right] < M:
        left+=1
    else:
        right-=1

print(result)
        