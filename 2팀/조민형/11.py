def max_sum(left, right):
    if left + 1 == right or left == right: return A[left]
    m = (left+right) // 2

    L = max_sum(left, m)
    R = max_sum(m,right)

    tmp = 0
    lside = float('-inf')
    for i in range(m, left-1, -1):
        tmp += A[i]
        lside = max(lside, tmp)
    
    tmp = 0
    rside = float('-inf')
    for i in range(m+1, right+1):
        tmp += A[i]
        rside = max(rside, tmp)
    
    M = lside + rside
    return max(L,R,M)

A = [int(x) for x in input().split()]
sol = max_sum(0, len(A)-1)
print(sol)