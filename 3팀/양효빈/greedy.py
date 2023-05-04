# 01. 모험가 길드
N = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

cnt = 0
idx = arr[0]

while True:
    if idx <= len(arr):
        arr = arr[idx:]
        cnt += 1
    else: break
    
    if len(arr) == 0:
        break
        
    idx = arr[0]
    
print(cnt)





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





# 05. 볼링공 고르기
N, M = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
result = []

for i in range(N):
    for j in range(i+1, N):
        if arr[j] != arr[i]:
            result.append([arr[i], arr[j]])
            
            
len(result)