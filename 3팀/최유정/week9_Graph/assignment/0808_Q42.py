# 탑승구
g = int(input())
p = int(input())
airplane = []
for _ in range(p):
    airplane.append(int(input()))
cnt = 0
airplane.sort(reverse=True)

idx = g

for a in airplane:
    if idx == 0:
        break
    if a < idx:
        idx = a-1
        cnt += 1
    else:
        idx -= 1
        cnt += 1

print(cnt)