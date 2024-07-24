n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
answer = []
total = 2e9

def check_pair(i:int, target:int):
    global liquids
    start, end = i, n-1
    idx = n-1
    while start < end:
        mid = (start+end)//2
        if liquids[mid] == target:
            return mid
        if liquids[mid] > target:
            end = mid - 1
            idx = mid
        else:
            start = mid + 1
    # print(lst, start, end, target)
    return idx

if liquids[0] * liquids[-1] > 0:
    if liquids[0] > 0:
        answer = liquids[:2]
    else:
        answer = liquids[-2:]
else:
    for i in range(n):          
        pair_liquid = check_pair(i+1, -liquids[i])
        
        if i+1 <= pair_liquid-1 < n and abs(liquids[i]+liquids[pair_liquid-1]) < total:
            total = abs(liquids[i]+liquids[pair_liquid-1])
            answer = [liquids[i], liquids[pair_liquid-1]]
        if total == 0:
            break
        
        if i+1 <= pair_liquid < n and abs(liquids[i]+liquids[pair_liquid]) < total:
            total = abs(liquids[i]+liquids[pair_liquid])
            answer = [liquids[i], liquids[pair_liquid]]
        if total == 0:
            break

print(*answer)