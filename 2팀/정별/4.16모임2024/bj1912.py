import sys
n= int(input())
A = list(map(int, sys.stdin.readline().split()))

max_sum = A[0]
cur_sum = A[0]

for elem in A[1:]:
    
    cur_sum = max(elem, cur_sum+elem)#아예 elem이 크거나.
    #cur_sum이 음수가 되었다면.
    #elem이 음수/양수든 뭘 더하든 작아지니까 무조건 elem 선택.
     #곧, 이전까지 쌓아온 cur_sum이 초기화되고 elem부터 다시 시작
    #혹시 몰라 max_sum에 최곳값이었던 cur_sum 저장

    max_sum = max(max_sum, cur_sum)
print(max_sum)

# dp = [0]*n
# dp[0] = A[0]

# for i in range(1, n):

#         dp[i] = max(A[i], dp[i-1]+A[i])



# i = 0
# j = 1
# cnt = A[0]
# nList=[]

# while i>n and j>n:
    
#     if cnt > cnt+A[j]:
#         i+=1
#         j+=1
#         cnt = A[i]
    
#     else:
#         cnt += A[j]
#         cnt.append(nList)
#         j+=1
# print(max(nList))


# A.sort(reverse=False)
# ans = 0
# for elem in A:
#     ans = max(ans, ans+elem)
# print(ans)