import sys
input = sys.stdin.readline

#쭉 펼쳐서 비교
 #둘 사이 거리랑 전체에서
col, row = map(int, (input().split()))
n = int(input())

nDirLoc= [list(map(int, input().split())) for _ in range(n)] #위치와 방향
nDGdir, nDGloc = map(int, input().split())
nDirLoc.append([nDGdir, nDGloc])

nPos = [] #바뀔 위치 좌표 저장
for ndir, nloc in nDirLoc:
    
    pos = 0
    if ndir == 1: pos = col - nloc
    if ndir == 2: pos = row + col + nloc
    if ndir == 3: pos = col + nloc
    if ndir == 4: pos = 2*(col+row) - nloc
    
    nPos.append(pos)

nDGloc_convert = nPos.pop()
cnt = 0

for now_pos in nPos:
    nloc1 = abs(nDGloc_convert - now_pos) #경우의수 1
    nloc2 = 2*(col+row) - nloc1
    
    cnt += min(nloc1, nloc2)
print(cnt)
