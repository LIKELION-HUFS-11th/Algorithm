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
