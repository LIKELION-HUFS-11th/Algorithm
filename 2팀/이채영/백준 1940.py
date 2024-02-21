N = int(input())
M = int(input())

ingredients = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if ingredients[i] == -1:
        continue

    need = M - ingredients[i]
    if need in ingredients:
        cnt += 1
        ingredients[ingredients.index(need)] = -1

    print(ingredients)

print(cnt)