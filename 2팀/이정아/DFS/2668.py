import sys
input = sys.stdin.readline

n = int(input())
seconds = [0]
answers = []
for _ in range(n):
    seconds.append(int(input()))

def dfs(x):
    global visited
    if seconds[x] in visited:
        return seconds[x]
    visited.add(seconds[x])
    return dfs(seconds[x])

for i in range(1, n+1):
    visited = set([])
    visited.add(i)
    if dfs(i) == i:
        answers.append(i)

print(len(answers))
for answer in answers:
    print(answer)