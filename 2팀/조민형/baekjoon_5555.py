import sys

searchString = sys.stdin.readline().rstrip("\n")
T = int(sys.stdin.readline())
result = 0

for i in range(T):
    ringString = sys.stdin.readline().rstrip('\n') * 2
    if searchString in ringString:
        result += 1

print(result)
    
