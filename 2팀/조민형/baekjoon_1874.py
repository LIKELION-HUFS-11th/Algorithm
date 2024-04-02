import sys

n = int(sys.stdin.readline())
stack = []
result = []
no_more_push = 0
is_possible= True


for i in range(1, n + 1):
    # 값 받기
    num = int(sys.stdin.readline())
    
    # 계속해서 값까지 올 때까지 스택에 추가
    while no_more_push < num:
        no_more_push += 1
        stack.append(no_more_push)
        result.append('+')
        
    # 맨 끝에 있는 값이 받은 값일 경우
    if stack[-1] == num:
        # 스택에서 빼기
        stack.pop()
        # 결과에는 - 추가
        result.append('-')
    else:
        # 아예 불가능한 경우 False값을 따로 설정해서 안될 경우에는 'NO'를 출력하도록 만들기
        is_possible = False
        
if is_possible:
    for j in result:
        print(j)
else:
    print("NO")

    
# import sys

# n = int(sys.stdin.readline())
# stack = [i for i in range(n,0,-1) ]

# real_list = []
# seq_list = []
# isReal = True
# def search(num):
#     global isReal
#     if real_list:
#          a = real_list[-1]
#          if a == num:
#              seq_list.append("-")
#              real_list.pop()
#              return
#          elif a < num and stack:
#              seq_list.append("+")
#              real_list.append(stack.pop())
#              return search(num)
#          elif a > num and real_list:
#              seq_list.append("-")
#              stack.append(real_list.pop())
#              return search(num)
#          else: 
#             isReal = False
#             return
#     elif stack:
#         seq_list.append("+")
#         real_list.append(stack.pop())
#         return search(num)
#     else: 
#         isReal = False
#         return

# for _ in range(n):
#     b = int(sys.stdin.readline())
#     search(b)
# print(stack, real_list)
# if isReal:
#     for k in seq_list:
#         print(k)
# else:
#     print('NO')


    

    
    
    
        
            
            