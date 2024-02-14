def old_knight():
    n, m = map(int, input().split())
    
    if n == 1:
        return 1
    elif n == 2:
        return min(4, (m+1) // 2)
    elif m <= 6:
        return min(4, m)
    else:
        return m-2
    
    
print(old_knight())