# 정말 이상하지만 이건 pypy3을 써야함..

X = input()
Y = input()

x = len(X)
y = len(Y)

DP = [[0 for _ in range(y+1)] for _ in range(x+1)]

for i in range(x+1):
    DP[i][0] = 0
for j in range(y+1):
    DP[0][j] = 0

result = 0

for i in range(1, x+1):
    for j in range(1, y+1):
        if X[i-1] == Y[j-1]: #공통 부문자열 발견
            DP[i][j] = DP[i-1][j-1] + 1
            if result < DP[i][j]:
                result = DP[i][j]

        # 만약 연속하지 않아도 부문자열이 가능하다면
        # else:
        #     DP[i][j] = max(DP[i][j-1], DP[i-1][j])


print(result)

