import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
#arr은 이미 정렬된 상태

left, right = 0, N-1
value = sys.maxsize

ans = []
while left < right: #겹치거나 넘어가면 끝
    if abs(arr[left]+arr[right]) <= value:
        ans = [arr[left], arr[right]] #ans에 두 용액 넣기
        value = abs(arr[left]+arr[right]) #value에는 두 용액으로 만들 수 있는 현재값
        
    if arr[left]+arr[right] < 0: #더 큰수 더해야함
        left += 1
    elif arr[left]+arr[right] > 0: #더 작은수 더해야함
        right -= 1
    else:
        break

print(*ans)