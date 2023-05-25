# 02. 곱하기 혹은 더하기
S = input()
arr = []

for i in range(len(S)):
    if int(S[i]) != 0: # 0일 때 덧셈이 필요한데 0의 덧셈은 결과에 영향을 주지 않으므로 0 포함하지 않음
        arr.append(int(S[i]))
    
result = 1
for num in arr:
    result *= num # 0을 제외한 모든 값을 서로 곱함
    
print(result)