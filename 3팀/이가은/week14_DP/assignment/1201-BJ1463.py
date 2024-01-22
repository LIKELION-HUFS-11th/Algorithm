n = int(input())

def calculation(num, cnt):
    if num == 1:
        return cnt
    
    if num % 3 == 0:
        return calculation(num//3, cnt + 1)
    elif num == 2:
        return calculation(num//2, cnt + 1)
    else:
        return calculation(num-1, cnt + 1)

print(calculation(n, 0))
