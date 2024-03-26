import sys

N = int(sys.stdin.readline())

N_enum = list(reversed(list(enumerate(map(int, sys.stdin.readline().split())))))
result = []

for i in N_enum:
    count = 0
    if result:
        for j in result:
            if count == i[1]:
                break
            if i[0] <= j:
                count+=1
    result.insert(count, i[0]+1)
for l in result: print(l, end=" ")
