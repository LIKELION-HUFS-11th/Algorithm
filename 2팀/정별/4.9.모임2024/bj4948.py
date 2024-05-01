import sys
#에라토스테네스의 체 개념 활용

#풀이1
#미리 소수 배열 만들기
nList = [0]*(123456*2+2) #n범위에서 2곱함+2

for i in range(2, 123456*2+1):
    for j in range(i, (123456*2+1)//i+1):
        if nList[i*j] != 0: #이미 다녀갔으면
            continue #시간단축
        else:
            nList[i*j] += 1

while True:
    n = int(sys.stdin.readline())
    if n==0:
        break #0이면 종료
    cnt = 0
    for k in range(n+1, 2*n+1):
        if not nList[k]: #0이라면
            cnt+=1
    print(cnt)
    
#풀이2: 입력받은 수마다 소수 확인해주기
#시간초과

# while True:
#     n = int(sys.stdin.readline())
#     if n==0:
#         break #0이면 종료
#     nList = [0] * (2*n+2)

#     for i in range(2, 2*n+1):
#         for j in range(2, (2*n+1)//i+1): #점점 범위가 줄어들음.i의 배수 체크
#             if nList[i*j] != 0:
#                 continue #시간단축
#             else:
#                 nList[i*j]+=1 #무언가의 배수인 합성수에는 모두 1더해짐
#     cnt = 0
#     for k in range(n, 2*n+1): #소수 걸러내기
#         if not nList[k]: #0인 소수라면
#             cnt += 1
#     print(cnt)
