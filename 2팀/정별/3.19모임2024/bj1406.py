#시간초과
import sys
sList = list(sys.stdin.readline().rstrip()) 
n=int(sys.stdin.readline().rstrip())

idx= len(sList)

commands = [sys.stdin.readline().split() for _ in range(n)]

for sElem in commands:
    # sElem =sys.stdin.readline().split()
    cm = sElem[0]
    if cm == 'L':
        if idx >0:
            idx -=1
    elif cm == 'D':
        if idx <= len(sList)-1:
            idx +=1
    elif cm == 'B':
        if idx >0:
            del sList[idx-1]
            idx-=1
    elif cm == 'P':
        sList.insert(idx, sElem[1])
        idx+=1
    else:
        continue


print(''.join(sList))
