import sys

# 커서 왼쪽에 들어있는 값을 스택처럼 처리
text1 = list(sys.stdin.readline().rstrip('\n'))
# 커서 오른쪽에 있는 값을 스택처럼 처리
text2 = []

for _ in range(int(sys.stdin.readline())):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if text1:
            text2.append(text1.pop())
    elif command[0] == "D":
        if text2:
            text1.append(text2.pop())        
    elif command[0] == "B":
        if text1:
            text1.pop()
    else:
        text1.append(command[1])

# 커서 오른쪽에 들어있는 스택의 경우 오른쪽에 있기 때문에 reverse 메서드를 통해 뒤집어주기
# 뒤집어준 후 커서 왼쪽 스택 다음에 붙여주기
text1.extend(reversed(text2))
print("".join(text1))
    
# 시간초과 나온 알고리즘
# index값을 커서로 사용해서 입력별 처리
# import sys

# fullText = list(sys.stdin.readline().rstrip('\n'))
# M = int(sys.stdin.readline())
# cursor = len(fullText)
# for _ in range(M):
#     command = sys.stdin.readline().split()
#     if command[0] == "L" or command[0] ==  "D":
#         if command[0] == "L" and cursor > 0:
#             cursor -=1
#         elif command[0] == "D" and cursor <= len(fullText):
#             cursor +=1
#     elif command[0] == "B":
#         if cursor-1 >= 0:
#             del fullText[cursor-1]
#             cursor -= 1
#     elif command[0] == "P":
#         fullText.insert(cursor,command[1])
#         cursor += 1
# print("".join(fullText))