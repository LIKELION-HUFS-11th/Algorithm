import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

friends = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    friends[a][b] = 1
    friends[b][a] = 1

invite = friends[1]
cnt = len(invite)
for friend in friends[1]:
    for f in friend:
        if f not in invite:
            invite.append(f)
            cnt += 1

print(cnt)