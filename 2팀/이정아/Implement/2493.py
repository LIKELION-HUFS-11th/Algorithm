n = int(input())
towers = list(map(int, input().split()))

'''
[구현] - 스택 활용
1. 자신 기준으로 (자기보다 왼쪽에 있음 and 자기보다 낮음)에 해당하는 탑은
어차피 이후에도 다시는 조회할 일 없음
1.1. 그래서 스택을 이용해 조건 1에 해당하는 탑 pop해서 버림
1.2. 그래서 탑은 왼쪽에서 오른쪽 순으로 조회
'''


stack = []
answer = [0] * n

for i in range(n): # 왼쪽에서 오른쪽 순으로 탑 조회
    while stack:
        if stack[-1][1] > towers[i]: # 스택 중 가장 오른쪽에 위치한 탑이 i보다 높으면
            answer[i] = stack[-1][0] # answer에 스택 중 가장 오른쪽에 위치한 탑 기록
            break # i에 대한 답 찾았으므로 더 이상 while문 안 돌아도 됨
        else: # 스택 중 가장 오른쪽에 위치한 탑이 i보다 낮으면(조건 1에 해당하면)
            stack.pop() # pop해서 버려버림
    stack.append([i+1, towers[i]]) # i도 나중에 쓰일 수 있으므로 일단 스택에 append

print(*answer)