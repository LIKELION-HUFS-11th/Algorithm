tower_count = int(input(""))
tower_list = list(map(int, input().split()))

stack = []
result = []

for i in range(tower_count):
    while stack:
        if stack[-1][1] > tower_list[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()

    if len(stack) == 0:
        result.append(0)

    stack.append((i, tower_list[i]))

print(*result)
