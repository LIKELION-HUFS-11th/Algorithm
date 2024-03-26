import sys
input = sys.stdin.readline

n = int(input())
count = 1
stack = []
ans = []
go = True

for _ in range(n) :
    num = int(input())
    # num 이하 숫자까지 스택에 push
    while count <= num :
        stack.append(count)
        ans.append('+')
        count += 1
    # num이랑 스택 맨 위 숫자가 동일하면 pop
    if stack[-1] == num :
        stack.pop()
        ans.append('-')
    # 스택 수열 만들기 불가
    else :
        go = False

if go :
    for x in ans:
    	print(x)
else:
    print("NO")

