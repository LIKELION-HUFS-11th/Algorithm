import sys

s = sys.stdin.readline().rstrip("\n")
result = []
for i in range(1,len(s)+1):
    for j in range(len(s)-i+1):
        result.append(s[j:j+i])
print(len(set(result)))
