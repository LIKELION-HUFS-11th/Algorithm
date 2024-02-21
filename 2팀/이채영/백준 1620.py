N, M = tuple(map(int, input().split()))

pockemon_names = {}
pockemon_nums = {}
for i in range(1, N+1):
    num = f"{i}"
    name = input()
    pockemon_names[name] = num
    pockemon_nums[num] = name

for i in range(M):
    target = input()
    if target.isdigit(): #문자열의 모든 문자가 숫자로만 이루어졌으면 True
        print(pockemon_nums[target])
    else:
        print(pockemon_names[target])
