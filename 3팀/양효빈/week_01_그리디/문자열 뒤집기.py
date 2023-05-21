# 03. 문자열 뒤집기
S = input()

# 0 -> 1
arr1 = S.split("1")

while "" in arr1: # 공백 삭제
    arr1.remove("")

cnt1 = 0
for s in arr1:
    if s in "0"*100000000: # 0을 연속으로 하는 긴 문자열 이용
        cnt1 += 1

# 1 -> 0
arr2 = S.split("0")

while "" in arr2: # 공백 삭제
    arr2.remove("")

cnt2 = 0
for s in arr2:
    if s in "1"*100000000:
        cnt2 += 1

print(min(cnt1, cnt2))