N = int(input())
num = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]

value = 1
a = N // 2 #행에서 왕래
b = N // 2 #열에서 왕래
arr[a][b] = value #맨 가운데 1 설정.

tmp = (N - 1) // 2 #총 도는 싸이클 횟수

for i in range(tmp): #위-오른쪽-아래-왼쪽 반복.
    #각 싸이클마다 이동할 횟수 조절. 싸이클 지나며 한 방향으로 가는 범위 점차 증가함
    # 위로 이동
    for _ in range(2 * i + 1):
        value += 1
        a -= 1
        arr[a][b] = value
    # 오른쪽으로 이동
    for _ in range(2 * i + 1):
        value += 1
        b += 1
        arr[a][b] = value
    # 아래로 이동
    for _ in range(2 * i + 2): #아래랑 왼쪽은 이전 크기에서 1개가 더 커짐.
        value += 1
        a += 1
        arr[a][b] = value
    # 왼쪽으로 이동
    for _ in range(2 * i + 2):
        value += 1
        b -= 1
        arr[a][b] = value

for _ in range(2 * (tmp - 1) + 2):
    value += 1
    a -= 1
    arr[a][b] = value

x = 0
y = 0
for i in range(N): #arr돌면서 출력하기
    for j in range(N):
        print(arr[i][j], end=" ")
        
        if arr[i][j] == num: #num 찾으면 x, y에 저장
            x = i + 1
            y = j + 1
    print()

print(x, y)