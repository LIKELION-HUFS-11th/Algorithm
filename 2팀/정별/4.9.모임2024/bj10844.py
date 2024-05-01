N = int(input())

# DPtable 초기화
a = [[0] * 10 for _ in range(N)]

# 1층 초값 설정
a[0] = [0,1,1,1,1,1,1,1,1,1]

# 점화식 구현
#a[n][k]는 n자리수에서 끝에 값이 k인 경우의수 총합
for n in range(1,N):
    a[n][0] = a[n-1][1] # 끝자리가 0
    a[n][9] = a[n-1][8] # 끝자리가 9
    
    for k in range(1,9): # 끝자리가 1~8
        a[n][k] = a[n-1][k-1] + a[n-1][k+1]
        
print(sum(a[N-1])%1000000000) # 0부터 시작해서 N자리수는 N-1로 접근




# n = int(input())

# def stair(n, cnt):
#     if n == 1: return 9
#     if n == 2: return 17
    
#     # cnt +=1
    
#     for i in range(1, 9):
        
    
#     for i in range(n):
#         if i == 0: continue
        
#         cnt += stair(i, cnt)
    
#     return cnt

# print(stair(n, 0))
    