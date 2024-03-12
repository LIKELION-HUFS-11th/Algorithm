import sys

result =[]
def is_possible(round,m,n):
    global result
    if m>n :
        rest_round = round-m
        if rest_round + n + 2 >= m:
            result.append(1)
        else: result.append(0)
    if m<n:
        rest_round = round-n
        if rest_round+m+1 >= n:
            result.append(1)
        else: result.append(0)
    if m==n:
        result.append(1)


round = int(sys.stdin.readline())
questions = int(sys.stdin.readline())

for i in range(questions):
    M, N = map(int,sys.stdin.readline().split())
    is_possible(round,M,N)

for j in result:
    print(j)
