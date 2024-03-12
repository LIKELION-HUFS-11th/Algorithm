
N = int(input())

total = 0
for i in range(1, N+1):
    num_list = list(map(int, list(str(i))))

    # if len(num_list) == 1:
    #     total += 1
    
    # elif len(num_list) == 2:
    #     if num_list[1] - num_list[0]:
    #         total += 1

    if len(num_list) < 3:
        total += 1
    
    else: #len(num_list) == 3
        if num_list[2] - num_list[1] == num_list[1] - num_list[0]:
            total += 1
        else:
            continue

print(total)