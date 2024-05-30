n = int(input())
values = list(map(int, input().split()))

ans = float("INF")
ans_left, ans_right = 0, 0

for i in range(n-1):
    current = values[i]
    start, end = i+1, n-1
    
    while start <= end:
        mid = (start+end)//2
        tmp = current+values[mid]
        
        if abs(tmp) < ans:
            ans = abs(tmp)
            ans_left = i
            ans_right = mid
            
            if tmp == 0:
                break
        
        if tmp < 0:
            start = mid+1
        else:
            end = mid-1

print(values[ans_left], values[ans_right])