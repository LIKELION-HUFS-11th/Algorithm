N = int(input())
p_list = list(map(int, input().split(" ")))
result = []

for i in range(N-1, -1, -1):
    result.insert(p_list[i], i+1)

for i in result:
    print(i, end=" ")