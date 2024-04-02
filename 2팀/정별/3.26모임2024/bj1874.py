n = int(input())

stack, res = [], []
flag = True

pointer = 1

for _ in range(n):
    nInput = int(input())

    while nInput >= pointer: #지금 수 나올 때까지 push
        stack.append(pointer)
        res.append('+')
        pointer+=1
    #다 쌓았으면
    if stack[-1] == nInput: #입력값이랑 스택 맨윗값
        stack.pop() #꺼내는 것임
        res.append('-')
    else: #다 쌓았는데도, 입력값이랑 스택 맨 위랑 다르면
        flag = False
        break
if not flag:
    print('NO')
else:
    for elem in res:
        print(elem)
    