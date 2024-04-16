import sys
# from collections import defaultdict

n = int(input())
A = list(map(int, sys.stdin.readline().split()))

dp= [1]*n #각 원소 자리에 부분 수열 크기 저장

for i in range(1,n):
    for j in range(0, i):#i이전까지 돌음
        
        if A[j]< A[i]:
            dp[i] = max(dp[i], dp[j]+1)#바로 이전까지 갱신되었던 값인지
                #증가 직전인 부분수열의 크기가 더 큰지 비교
print(max(dp))

# n_A = set(A)
# dic_A = {0:0}

# for i, elem in enumerate(A):
    
#     if elem in dic_A:
#         # dic_A[elem] = [dic_A[elem], i]
#         dic_A[elem].append(i)
#     else:
#         dic_A[elem] = dic_A.get(elem, [i])
# # print(dic_A)
# dic_A = sorted(dic_A.items())
# print(dic_A)

# for i, n_dic in enumerate(dic_A):#key들만 뽑기
    
#     pnt = 0 #value 안에서 포인터
#     cnt = 0
#     n_list=[]
#     while TRUE:
#         if i == len(dic_A):
            
            
#         i+=1
#         if n_dic[0] <= dic_A[i][0]: #증가하는 부분 수열 아니면
            
#         else:
#             n_list.append(dic_A[i][0])
        
        
#     print(n_dic[1])