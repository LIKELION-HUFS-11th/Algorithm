# 1 ~ N개 헛간 -> 골라숨기 -> 1번 헛간으로부터 최단 거리가 가장 긴 헛간
# 최단거리 = 지나야 하는 길의 최소 개수
# 술래는 1번 헛간에서 출발
# M개의 양방향 통로

# 출력 = 숨을 헛간 번호(같은 헛간이 여러 개면 가장 작은 헛간 번호 출력), 그 헛간까지의 거리, 그 헛간과 같은 거리를 갖는 헛간의 개수
# 1번 헛간으로부터의 최단거리 중 최댓값 찾기(max)

INF = int(1e9)
n, m = map(int, input().split())

# (n+1) X (n+1) 2차원 arr
arr = [[INF] * (n+1) for _ in range(n+1)]

# 대각행렬 = 0
for i in range(1, n+1):
    arr[i][i] = 0

# 연결된 헛간 1로 갱신하기
for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1


# 최단거리 갱신하기(min)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            arr[a][b] = min(arr[a][b], arr[a][k] + arr[k][b])


result = 0  # 헛간까지의 거리
num = 0  # 숨을 헛간 번호

for i in range(1, n+1):
    tmp = arr[1][i]
    if tmp != INF and result < tmp:
        result = tmp
        num = i

# 같은 거리 헛간 개수 세기
cnt = 0
for i in range(1, n+1):
    if arr[1][i] == result:
        cnt += 1


print(num, result, cnt)

