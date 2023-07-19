# 모험가 길드

# N : 모험가 수
N = int(input())
adven = list(map(int, input().split()))
adven.sort(reverse=True)
result = []
cnt = 0

while adven != []:
    a = adven.pop()
    result.append(a)
    if a == len(result):
        result = []
        cnt += 1

print(cnt)