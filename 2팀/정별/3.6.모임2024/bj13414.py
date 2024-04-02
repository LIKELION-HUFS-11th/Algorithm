import sys
input = sys.stdin.readline

k, l = map(int, input().split())   # k: 수강 가능 인원, l: 대기 목록 길이
dict = {}
for i in range(l):
  dict[input().strip()] = i

sorted_dict = sorted(dict.items(), key=lambda x: x[1])

for i in range(k):
  if i < len(sorted_dict):
    print(sorted_dict[i][0])
  else:
    break