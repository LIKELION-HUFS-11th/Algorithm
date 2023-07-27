# 편집거리

# 연산 : 삽입, 삭제, 교체
# 문자열 길이 : 1~5000

A = input()
B = input()
a_len = len(A)
b_len = len(B)

dp = [[0 for _ in range(a_len+1)] for _ in range(b_len+1)]
for i in range(a_len+1):
    dp[0][i] = i
for i in range(b_len+1):
    dp[i][0] = i

# 이중 for문 -> 10^6
for i in range(1, b_len+1):
    for j in range(1, a_len+1):
        if (i==j and A[j-1]!=B[i-1]):  # ab de -> abc def (교체+1)
            dp[i][j] = dp[i-1][j-1]+1
        elif(A[j-1]==B[i-1]):          # ab de -> abc dec (변함없음)      abc de -> abcd ded (변함없음)
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1  # abc de(+1) // abcd de(변함없음)  //  abc def (+1) ->  abcd def

print(dp[b_len][a_len])