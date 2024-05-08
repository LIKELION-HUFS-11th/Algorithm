import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]

dr = [0, 1, 0, -1] # 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
dc = [1, 0, -1, 0]

r = n//2  # 시작 row
c = n//2  # 시작 column
num = 1  # 해당 위치에 들어갈 숫자 1씩 증가 예정
len = 0  # 특정 방향으로 이동할 길이 얼마나 더할 것인가. for 문으로 동일 작업 수행 가능.

board[r][c] = num

while True:
    for i in range(4):
        for _ in range(len):  # 특정 방향으로 한칸씩 이동하며 숫자 입력
            r+=dr[i]
            c+=dc[i]
            num+=1
            board[r][c]=num
            if num==m:  # 찾을 번호의 인덱스 저장
                ans = [r+1, c+1]

    if r==c==0:
        break
    r -= 1
    c -= 1
    len += 2

for i in range(n):
    print(*board[i])
print(*ans)