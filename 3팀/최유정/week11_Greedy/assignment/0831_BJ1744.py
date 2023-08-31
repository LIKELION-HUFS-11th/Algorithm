def func1(list):
    l = len(list)
    total = 0
    if l > 1:
        for i in range(0, l-1, 2):
            total += (list[i] * list[i+1])
        if l % 2 != 0:
            total += list[l-1]
    else:
        total += list[0]
    return total

n = int(input())
minus_list = []
plus_list = []
total = 0
for _ in range(n):
    i = int(input())
    if i <= 0:
        minus_list.append(i)
    elif i > 1:
        plus_list.append(i)
    elif i == 1:
        total += 1

minus_list.sort()
plus_list.sort(reverse=True)

if minus_list != []:
    total += func1(minus_list)
if plus_list != []:
    total += func1(plus_list)
print(total)