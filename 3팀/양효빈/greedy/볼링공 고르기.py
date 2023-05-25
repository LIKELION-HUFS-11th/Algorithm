# 05. 볼링공 고르기
N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
result = []

for i in range(N):
    for j in range(i+1, N):
        if arr[j] != arr[i]:
            result.append([arr[i], arr[j]])
            
            
len(result)