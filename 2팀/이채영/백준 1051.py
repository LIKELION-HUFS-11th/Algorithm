import sys
input = sys.stdin.readline

global rec, n, m

# 0~n-1, 0~m-1
def find_square(l): # l <= m, l <= n
    global rec, n, m

    for i in range(0, n-l+1): #행
        for j in range(0, m-l+1): #열
            # 세번째 조건 주의
            if rec[i][j] == rec[i][j+l-1] and rec[i][j] == rec[i+l-1][j] and rec[i][j] == rec[i+l-1][j+l-1]:
                return l * l

    return -1



n, m = map(int, input().split()) #n = 세로 m = 가로
max_len = min(n, m) #정사각형의 최대 가로길이
# 정사각형 길이가 1 ~ max_len일때 하나하나 확인



rec = []
for _ in range(n):
    nums = list(input().strip())

    rec.append(nums)



for l in range(max_len, 0, -1):
    result = find_square(l)
    if result == -1:
        continue
    else: #최대 크기 발견
        break

print(result)