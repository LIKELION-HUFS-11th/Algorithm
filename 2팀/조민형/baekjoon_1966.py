import sys

T = int(sys.stdin.readline())
for _ in range(T):
    m, n = map(int,sys.stdin.readline().split())
    pr = []
    print_list = list(map(int, sys.stdin.readline().split()))
    pr = [(i, num) for i, num in enumerate(print_list)]
    count = 1
    while pr:
        if pr[0][1] >= max(pr,key=lambda x: x[1])[1]:
            if pr[0][0] == n:
                break
            count+=1
            pr.pop(0)
        else:
            pr.append(pr.pop(0))
    print(count)
    