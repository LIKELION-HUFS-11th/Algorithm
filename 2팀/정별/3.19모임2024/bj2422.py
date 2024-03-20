n, m = map(int, input().split())
ices = [[True for _ in range(n)]for _ in range(n)]



for i in range(m):
    a, b = ((lambda x: x-1)(i) for i in (map(int, input().split())))
    ices[a][b] = ices[b][a] = False

result = 0
for one in range(n):
    for two in range(one+1, n):
        for three in range(two+1, n):
            if ices[one][two] and ices[one][three] and ices[two][three]:
                result += 1
print(result)