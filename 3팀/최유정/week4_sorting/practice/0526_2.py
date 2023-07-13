# 위에서 아래로

N = int(input())
num_list = [int(input()) for _ in range(N)]
num_list.sort()

for n in num_list:
    print(n, end=" ")