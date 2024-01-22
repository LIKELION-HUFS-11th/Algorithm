import sys
sys.setrecursionlimit(10001)

n = int(sys.stdin.readline())
schedule = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    schedule.append((s, e))

schedule.sort(key = lambda x: x[1])
# print(schedule)

classes = []

def check_room(start, end):
    for i in range(len(classes)):
        if classes[i] <= start:
            classes[i] = end
            return 0
    classes.append(end)
    return 1

ans = 0
for s, e in schedule:
    ans += check_room(s, e)

print(ans)




