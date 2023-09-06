#입력
r,c = tuple(map(int,input().split()))

arr_2d = [
    list(input().split())
    for _ in range(c)
]

#이동 가능한 경우의 수


# W -> (B) -> (W) -> B
# W -> (B) -> (W) -> B
# B -> (W) -> (B) -> W

cnt = 0

for i in range(r-2):
    for j in range(c-2):
        for k in range(i+1,r-1):
            for l in range(j+1, c-1):
                if arr_2d[0][0] != arr_2d[i][j] and arr_2d[i][j] != arr_2d[k][l] and arr_2d[k][l] != arr_2d[r-1][c-1]:
                    cnt+=1
print(cnt)