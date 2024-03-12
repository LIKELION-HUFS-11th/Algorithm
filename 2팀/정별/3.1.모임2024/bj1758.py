import sys
n = int(input())
nArr = [int(sys.stdin.readline()) for _ in range(n)]
nArr = sorted(nArr, reverse= True)

cnt = 0
for i, elem in enumerate(nArr):
    x= elem - i
    if x>0:
        cnt += x
print(cnt)
