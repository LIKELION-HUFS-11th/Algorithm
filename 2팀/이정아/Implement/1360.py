import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

commands = [] # 명령어 리스트
types = deque([]) # 출력할 문자열 리스트
for _ in range(n):
    commands.append(list(input().split()))

# undo도 undo될 수 있음 => 맨 뒤의 명령어부터 처리하기 위해 idx를 맨 뒤로 설정
idx = n-1
while idx >= 0: # 모든 명령어 다 돌 때까지
    if commands[idx][0] == "type": # type이면
        types.appendleft(commands[idx][1]) # 맨 뒤 명령어부터 처리하므로 appendleft
        idx -= 1
    if commands[idx][0] == "undo": # undo면
        rollback = int(commands[idx][2]) - int(commands[idx][1]) # rollback 시점의 명령어까지 무시해야 함
        if idx == 0: # 맨 첫번째 명령어까지 왔는데 undo면 더 undo할 게 없으므로 break
            break
        if rollback > int(commands[idx-1][2]): # 현재 명령어 바로 앞 명령어의 시점이 rollback보다 적으면 continue
            idx -= 1
            continue

        while True: # rollback 시점에 실행된 명령어 찾을 때까지 idx -= 1
            idx -= 1
            if idx == -1: # rollback 시점에 실행된 명령어가 끝까지 없으면 break
                break
            if rollback > int(commands[idx][2]): # rollback 시점까지 왔으면 break
                break

for s in types:
    print(s, end="")
print() 
            