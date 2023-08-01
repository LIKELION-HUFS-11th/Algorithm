stack = []

#삽입: append(), 삭제: pop()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) #디폴트는 맨 아래부터 시작
print(stack[::-1]) #최상단원소부터