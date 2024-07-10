import math
n = int(input())

# def get_primary_list(n): #이거쓰니까 시간초과
#     array = [1 for _ in range(n+1)]

#     for i in range(2, int(n ** 0.5) + 1):
#         if array[i]:
#             j = 2

#         while i * j <= n:#합성수로 표시
#             array[i * j] = 0
#             j += 1

#     return array
def isPrime(x): # 소수인지 판별해주는 함수
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

res = 0
for i in range(n, 1000001): # 입력값 N 부터 최대값 까지 순환
    if i == 1: # 1은 소수가 아니기 때문에 예외처리
        continue
    if str(i) == str(i)[::-1]: # 팰림드롬 수 일 경우
        if isPrime(i) == True: # 소수 판별
            res = i
            break

if res == 0: # 입력값이 만약 최대 값 100만일 경우
    res = 1003001 # 100만 이상이면서 팰림드롬 및 소수일 경우를 적용

print(res)