from copy import deepcopy

def find_max_total(result, cnt):
    if (cnt == n):
        return max(arr[n-1])
    for i in range(len(result)):
        arr[cnt][i] = max(arr[cnt][i], result[i] + answer[cnt][i])
        arr[cnt][i+1] = max(arr[cnt][i+1], result[i] + answer[cnt][i+1])
    return find_max_total(arr[cnt], cnt+1)

n = int(input())

arr = []

for i in range(n):
    temp = list(map(int, input().split(" ")))
    arr.append(temp)

answer = deepcopy(arr)

print(find_max_total(arr[0], 1))