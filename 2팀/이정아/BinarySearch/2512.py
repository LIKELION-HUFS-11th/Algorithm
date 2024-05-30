n = int(input())
requests = list(map(int, input().split()))
budget = int(input())
total = sum(requests)

if total <= budget:
    print(max(requests))

else: 
    requests.sort()
    idx = 0
    avg = budget//n
    while idx <= n-1:
        if requests[idx] > avg:
            print(avg)
            break
        for i in range(idx, n):
            if requests[i] <= avg:
                idx += 1
                budget -= requests[i]
            else:
                break
        avg = budget//(n-idx)