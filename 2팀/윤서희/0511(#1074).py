import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0

while n != 0:
    n -= 1
    row = 2 ** n

    # 1사분면
    if r < row and c < row:
        cnt += 0 
    # 2사분면
    elif r < row and c >= row:
        cnt += row * row
        c -= row
    # 3사분면
    elif r >= row and c < row:
        cnt += row * row * 2
        r -= row
    # 4사분면
    else:
        cnt += row * row * 3
        r -= row
        c -= row

print(cnt)