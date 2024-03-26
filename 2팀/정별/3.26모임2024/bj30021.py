#별 쌩난리를 피웠지만,
#n(n+1)/2와 합성수 관계만 알면 매우 쉽게 풀리는..

#난리의 흔적
N = int(input())

def is_prime(n): #Miller-Rabin 소수 판별법
    if n<=1:
        return False
    if n<=3: 
        return True

    if n%2 == 0 or n %3 == 0:
        return False
    
    i=5
    while i*i <=n:
        if n % i == 0 or n %(i+2)== 0:
            return False
        i += 6
    return True

def decimal(n): #nAr에 차있으면 합성수, 0이면 소수
    global nAr
    nAr = [0] * (n+1)

    for i, elem in enumerate(nAr):

        if elem or i == 0 or i == 1: #elem이 1이상이면
            continue #다음 i로 넘어감
        for j in range(1, n//i +1):
            if j == 1:
                continue
            nAr[i * j] +=1


def solve(n):
    Sn = N*(1+N)>>1 #1부터 N까지의 합. 비트시프트 사용

    nAr =[0] * (Sn+1)
    decimal(Sn)

    #선물 순서 저장
    order=[]
    
    

decimal(Sn) #최대 합까지 다 채워두기
# if not nAr[-1]:
#     print('NO')
# else:
#     print("YES")
#     left=1
#     right=N
    
#     cnt = 0 #선물받은 수들의 합

#     nList = [0]*N
#     while cnt <= Sn:
        
        
#         # cnt += left
#         if nAr[cnt + left] == 0: #다음 left을 합한값이 소수이라면
#             if nAr[right] == True: #N이 합성수라면
#                 cnt += right
            
#             else:
                
#         left+=1
        
nDecimal =[] #소수 숫자 보관
for i in range(2, len(nAr)):
    if nAr[i] == 0:
        nDecimal.append(i)

ans=[]
cnt = 0
for i in range(1, N+1):
    
    if cnt+i in nDecimal:
        continue
    else:
        cnt +=i #cnt =1
        ans.append(i)
    
print(nAr)

def sum_decimal(n):
    
    if n in nDecimal: #소수라면
        return n
    else:
        cnt += n
        return sum_decimal(cnt)

#정답!!!!!ㅠㅠㅠ
n = int(input())

if n== 1:
    print('YES')
    print(1)
elif n == 2:
    print('NO')
elif n == 3:
    print('YES')
    print(1, 3, 2)
else:
    print('YES')
    print(1, 3, 2, end=' ')
    for i in range(4, n+1):
        print(i, end=' ')