def get_primary_list(n):
    array = [1 for _ in range(n+1)]

    for i in range(2, int(n ** 0.5) + 1):
        if array[i]:
            j = 2

        while i * j <= n:
            array[i * j] = 0
            j += 1

    return array

T = int(input())
nums = [int(input()) for _ in range(T)]
max_num = max(nums)
primarys = get_primary_list(max_num)

for num in nums:
    result = 0

    for i in range(2, num // 2 + 1):
        if primarys[i] and primarys[num - i]:
            result += 1

    print(result)
    
# import sys, math

# T = int(input())
# nInputs = list(map(int, sys.stdin.readlines()))
# # print(max(nInputs))
# nRange = max(nInputs)

# nDecimals =[0] * (nRange+1)
# nDecimals[0], nDecimals[1] = 1, 1 #0과 1도 소수 아니니까 합성수 처리
# # Flag=False

# for i in range(2, int(round(math.sqrt(nRange), 0))+1):
#     if not nDecimals[i]:
#         for j in range(i*2, nRange+1, i):
#             nDecimals[j] +=1
# sosu =[]
# for i in range(nRange+1):
#     if not nDecimals[i]:
#         sosu.append(i)

# # print(nDecimals)

# for elem in nInputs:
#     cnt = 0
#     nList=[]
#     for i in range(len(sosu)):

#         for j in range(i, len(sosu)):
#             if sosu[i] + sosu[j] == elem:
#                 cnt+=1
#     print(cnt)

# # for _ in range(T):
# #     N = int(sys.stdin.readline())
# #     cnt =0
# #     nList=[] #3+5, 5+3 같은 중복 방지
# #     for i in range(2, N):
# #         if not nDecimals[i] and not nDecimals[N-i]:
# #             nCandis = sorted([i,N-i])
# #             if nCandis not in nList:
# #                 nList.append(nCandis)
# #                 cnt+=1
# #     # print(nList)
# #     print(cnt)