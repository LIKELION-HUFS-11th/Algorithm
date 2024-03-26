N, S = map(int, input().split())
arr = list(map(int, input().split()))
stlist = []
cnt = 0


def ar(start):
    global cnt
    if sum(stlist) == S and len(stlist) > 0:
        cnt += 1

    for i in range(start, len(arr)):
        stlist.append(arr[i])
        ar(i+1)
        stlist.pop()  


ar(0)
print(cnt)