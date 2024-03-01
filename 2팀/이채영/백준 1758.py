n = int(input())

customers = []
for _ in range(n):
    customers.append(int(input()))

customers.sort(reverse=True) #내림차순 정렬

total = 0
for i in range(n):
    tip = customers[i] - i
    if tip <= 0:
        continue
    else:
        total += tip

print(total)