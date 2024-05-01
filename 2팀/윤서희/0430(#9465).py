import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    stickers = []
    nums = list(map(int, input().split()))
    stickers.append(nums)
    nums = list(map(int, input().split()))
    stickers.append(nums)

    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
    else:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]

        for i in range(2, n):
            stickers[0][i] += max(stickers[1][i - 1], stickers[1][i - 2])
            stickers[1][i] += max(stickers[0][i - 1], stickers[0][i - 2])
        
        print(max(stickers[0][n - 1], stickers[1][n - 1]))



