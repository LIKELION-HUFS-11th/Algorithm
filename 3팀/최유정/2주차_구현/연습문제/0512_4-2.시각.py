N = int(input())
# 03, 13, 23, 33, 43, 53, 30, 31, 32, 34, 35, 36 ,37, 38, 39 -> 15가지
# 전체 ->60가지
total = (N+1)*60*60
f = N // 3

# 3이 포함안되어 있는 경우
cnt = (N+1-f)*45*45

print(total-cnt)