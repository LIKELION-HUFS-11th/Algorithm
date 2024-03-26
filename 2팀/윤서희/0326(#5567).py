import sys
input = sys.stdin.readline

n = int(input()) # 동기 수
m = int(input()) # 리스트 길이

info = [0] * (n + 1)
friends = []

for i in range(m):
    friend = list(map(int, input().split()))
    if friend[0] == 1 or friend[1] == 1:
        if friend[0] == 1:
            info[friend[1]] = 1
        else:
            info[friend[0]] = 1
    else:
        friends.append(friend)

friends2 = []
for i in friends:
    if info[i[0]] == 1 or info[i[1]] == 1:
        friends2.append(i)

for i in friends2:
    info[i[0]] = 1 
    info[i[1]] = 1

print(info.count(1))