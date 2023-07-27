jusik = [7, 1, 5, 3, 6, 4]
profit = 0
max = 0
for i in range(len(jusik)-1):
    for k in range(1, len(jusik)):
        profit = jusik[k] - jusik[i]
        if profit > max:
            max = profit

print(max)
