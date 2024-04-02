import sys
input = sys.stdin.readline

s = input()
cnt = 0
texts = set()

for i in range(0, len(s)):
    for j in range(i + 1, len(s)):
        # print(j, i, s[i:j])
        if s[i:j] not in texts:
            cnt += 1
            texts.add(s[i:j])
print(cnt)