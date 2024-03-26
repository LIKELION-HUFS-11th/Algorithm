import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
friends = dict()
result = []

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if a in friends:
        friends[a].append(b)
    else:
        friends[a] = [b]
    if b in friends:
        friends[b].append(a)
    else:
        friends[b] = [a]

if 1 in friends:
    for i in friends[1]:
        result.append(i)
        if i in friends:
            for j in friends[i]:
                result.append(j)
                
    print(len(set(result))-1)
else:
    print(0)

