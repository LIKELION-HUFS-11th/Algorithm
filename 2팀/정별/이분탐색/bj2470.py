import sys

n = int(input())
nList = list(map(int, sys.stdin.readline().split()))
nList.sort()

l = 0
r = len(nList)-1
m = len(nList)//2


def Search(l, r):
    if abs(l-r) ==1 or abs(r-l) ==1:
        return nList[l], nList[r]
    
    if nList[l] + nList[r]< 0:
        l +=1
    elif nList[l] + nList[r]>0:
        r -=1
    
    Search(l, r)


