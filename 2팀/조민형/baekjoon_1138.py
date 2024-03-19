import sys

N = int(sys.stdin.readline())

N_enum = list(reversed(list(enumerate(map(int, sys.stdin.readline().split())))))
result = []
print(N_enum)
for i in N_enum:
    count = 0
    for j in result:
        if i[0] <= j:
            count+=1
        print("count", count, "result", result, "j", j)
        if count == i[1]:
            break
    result.insert(count, i[0]+1)
    print(result)
print(result)
