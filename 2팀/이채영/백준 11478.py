import sys
input = sys.stdin.readline

"""
sol1) 시간초과
"""
s = list(input().strip())

words = {}

cnt = 0
for i in range(0, len(s)):
    k = s[i]
    if k not in words.keys():
        words[k] = []

    satisfied = False
    for j in range(i+1, len(s)+1):
        word = ''.join(s[i:j])

        if satisfied == False:
            if word in words[k]:
                continue
            else: #부분문자열 중복 없음 -> 이후로도 중복될 일 없음
                words[k].append(word)
                cnt += 1
                satisfied = True #이제 탐색 안해도 됨
        # if word in words[k]:
        #     continue
        else:
            words[k].append(word)
            cnt += 1

# print(words)
print(cnt)
    




"""
sol2) 집합 set 사용 - 걍 알아서 중복처리됨
"""
s = input().strip()
s_set = set()

for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        s_set.add(s[j:j+1])

print(len(s_set))