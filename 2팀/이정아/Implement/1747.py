import math

'''
[구현 + 수학]
1. 팰린드롬 만족
2. 소수 만족
3. n보다 크거나 같은 수 중 제일 작은 수
'''

n = int(input())

# 팰린드롬 체크
def is_palindrome(x:int):
    string_x = str(x)
    length = len(string_x)
    if length % 2 == 0:
        if string_x[:length//2] == string_x[length-1:length//2-1:-1]:
            return True
    else:
        if string_x[:length//2] == string_x[length-1:length//2:-1]:
            return True
    return False

# 소수 체크
def is_prime(x:int):
    maxnum = int(math.sqrt(x))
    for i in range(maxnum, 1, -1):
        if x % i == 0:
            return False
    return True

if n == 1:
    print(2)
else:
    ans = n
    while True:
        if is_palindrome(ans) and is_prime(ans): # 팰린드롬과 소수 만족할 시 프린트
            print(ans)
            break
        ans += 1 # 아니면 +1해서 다음 수 탐색