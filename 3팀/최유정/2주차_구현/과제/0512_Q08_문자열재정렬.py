from collections import deque

S = list(input())
S.sort()
S=deque(S)
cnt = 0


while True:
    if S[0] < 'A':
        cnt += int(S[0])
        S.popleft()
    else:
        break
result = ''.join(s for s in S)
result += str(cnt)
print(result)