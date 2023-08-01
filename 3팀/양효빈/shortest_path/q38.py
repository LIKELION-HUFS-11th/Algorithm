
n, m = map(int, input().split())
arr = [[int(1e9)] * (n+1) for _ in range(n+1)]

# 대각선 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            arr[a][b] = 0

# 각 간선에 대한 정보 입력받아 초기화
for _ in range(m):
    # A에서 B로 가는 비용 1로 설정
    a, b = map(int, input().split())
    arr[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])

result = 0

for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if arr[i][j] != int(1e9) or arr[i][j] != int(1e9):
            count += 1
    if count == n:
        result += 1

print(result)