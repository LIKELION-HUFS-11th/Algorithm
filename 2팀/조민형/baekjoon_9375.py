import sys

T = int(sys.stdin.readline())
result = []
for _ in range(T):
    C = int(sys.stdin.readline())
    closet = {}
    for _ in range(C):
        wearing, kind = sys.stdin.readline().rstrip('\n').split()
        if kind in closet:
            closet[kind] += 1
        else: closet[kind] = 1
    count_copy = 0
    if len(closet) == 1:
        for value in closet.values():
            count_copy += value
            result.append(count_copy)
    else: 
        new_count = 1
        for j in closet.values():
            new_count = new_count * (j+1)
        result.append(new_count - 1)

for k in result:
    print(k)