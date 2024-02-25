import sys

N = int(sys.stdin.readline())

people =[]
for i in range(N):
    tip = int(sys.stdin.readline())
    people.append(tip)

people.sort(reverse=True)
result = 0
for j in range(len(people)):
    rank = j+1
    if people[j] - (rank-1) < 0:
        pass
    else: result += people[j] - (rank-1)

print(result) 