import sys
input = sys.stdin.readline

# 아래, 오른쪽, 위로, 왼쪽
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
num = int(input())

arr = [[0] * n for _ in range(n)]


# 방향성의 규칙에 의한 -1 선언
d = -1

k = n ** 2

# 0,0 이 아닌 -1, 0 으로 배정이후 규칙성에 넣기
x, y = -1, 0

# 찾는 숫자 값 넣는 리스트
ans = []

for _ in range(n * 2 - 1):
    # 방향
    d = (d + 1) % 4

    # n번 만큼 움직인다.
    for _ in range(n):

        # 규칙성에 의해 값 플러스 하기
        x += dx[d]
        y += dy[d]

        # 해당 위치 k값으로 정의
        arr[x][y] = k

        # 만약 k가 찾는 수라면
        if k == num:
            ans.append((x + 1, y + 1))
        # k -= 1 진행하므로 달팽이 움직임을 보여주기
        k -= 1
    # 만약 아래로 내려가는 것 또는 위로 올라 가는 것이 끝났다면 n을 -1 더해서 n번 을 줄이기
    if not d or not d % 2:
        n -= 1
# 반복문을 이용하여 해당 인덱스 값을 Unpacking 통해 출력
for i in range(len(arr)): print(*arr[i])

# 위치값 Unpacking으로 출력
print(*ans[0])