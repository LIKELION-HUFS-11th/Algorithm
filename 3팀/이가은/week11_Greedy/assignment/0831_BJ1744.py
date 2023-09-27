'''
[수 묶기]
https://www.acmicpc.net/problem/1744

1. 음수는 음수끼리 양수는 양수끼리 곱한다
2. 0과 1은 더하기만 한다
3. 절대값이 큰 녀석끼리 우선적으로 곱한다
'''
n = int(input())
neg = []
pos = []

result = 0
for _ in range(n):
    num = int(input())
    if num < 0:
        neg.append(num)
    elif num > 0:
        pos.append(num)
    else:
        result += num
print(result)

neg.sort()
pos.sort(reverse=True)
if len(neg) % 2 == 1:
    result += neg[-1]
    neg.pop()
if len(pos) % 2 == 1:
    result += pos[-1]
    pos.pop()
print(result)

for i in range(1, len(neg), 2):
    result += neg[i] * neg[i - 1]
for i in range(len(pos), 2):
    result += pos[i] * pos[i - 1]
print(result)
print(neg, pos)


