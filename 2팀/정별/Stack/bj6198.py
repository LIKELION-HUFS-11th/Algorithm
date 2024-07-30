import sys

n = int(input())
nBuildings =list(int(sys.stdin.readline().strip()) for _ in range(n))
# print(nBuildings)
stack = []
cnt=0
stack.append(nBuildings[0])

#나를 내려다보는 왼쪽의 빌딩들 수를 세는 것임
    #단 왼쪽의 빌딩들 중에서 나보다 낮은 애는 스택에서 제외됨
    
for i in range(1, n):

    # print(stack, '12')
    while True:
        if len(stack) > 0 and stack[-1] <= nBuildings[i]:
            #스택에 있는 애들보다, 지금 수가 더 크면 
                #지금 수 보다 더큰 수 나올 때까지 지워줌.
                #그러다가 스택 비워지면 break
            stack.pop()
        else:
            break

    # print(stack, '19')
    cnt += len(stack)
    stack.append(nBuildings[i])

print(cnt)



#1. 이중for문은 당연히 안되고
# for i in range(n-1):
#     cnt = 0
#     j=i
#     while stack or j<n:
#         j+=1
#         if nBuildings[i]>nBuildings[j]:
#             stack.append(j)
            
#         else:
#             cnt+= len(stack)


#2. 거꾸로 왼쪽으로가면서 지나온 길에서 나보다 큰 애를 찾는 접근도 경우의수 너무 많음
# cnt=0
# flag = True
# nAns = [0 for _ in range(n)]

# vUpdown = False

# # vFlag = False

# nStack=[]
# for i in range(n-1, -1, -1):
    
#     if not vUpdown:
#         if stack and nBuildings[i]> nBuildings[stack[-1]]:
#             #바로 오른쪽 옆 빌딩이 나보다 작다면
#             nAns[i]+= (n-i-1)
#             stack.pop()
#             # stack.append(i)
        
#         elif stack and nBuildings[i]<= nBuildings[stack[-1]]:
#             vUpdown= True
#             continue

#         stack.append(i)

            
#     else:
#         while stack and nBuildings[i]> nBuildings[stack[-1]]:
#             stack.pop()
        
#         if stack:
#             nAns[i] += stack[-1] -i -1 #1칸 차이 나면 0으로 나타남
        
#         stack.append(i)



# print(nAns)