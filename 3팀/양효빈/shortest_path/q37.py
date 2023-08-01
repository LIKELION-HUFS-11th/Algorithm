
n = int(input())
m = int(input())
result = [ [int(1e9)]*(n+1) for _ in range(n+1)] # 무한으로 초기화

# 대각선 0으로 초기화
for i in range(1, n+1):
    result[i][i] = 0


# 정보 입력받아 초기화
for _ in range(m):
    a, b, c = map(int, input().split())
    # 가장 짧은 간선 정보만 저장
    if c < result[a][b]:
        result[a][b] = c


# 플로이드 워셜 알고리즘
# 그냥 다 돌아버리기(예외 생각 X, 어차피 시간복잡도 똑같으니 예외 설정하면 복잡하기만 함)
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            result[a][b] = min(result[a][b], result[a][k] + result[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우 0 출력
        if result[a][b] == int(1e9):
            print(0, end=" ")
        else:
            print(result[a][b], end = " ")
    
    print()














