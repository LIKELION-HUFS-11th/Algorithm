#정답 풀이
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


#시간초과
import sys
sList = list(sys.stdin.readline().rstrip()) 
n=int(sys.stdin.readline().rstrip())

idx= len(sList)

commands = [sys.stdin.readline().split() for _ in range(n)]

for sElem in commands:
    # sElem =sys.stdin.readline().split()
    cm = sElem[0]
    if cm == 'L':
        if idx >0:
            idx -=1
    elif cm == 'D':
        if idx <= len(sList)-1:
            idx +=1
    elif cm == 'B':
        if idx >0:
            del sList[idx-1]
            idx-=1
    elif cm == 'P':
        sList.insert(idx, sElem[1])
        idx+=1
    else:
        continue


print(''.join(sList))
