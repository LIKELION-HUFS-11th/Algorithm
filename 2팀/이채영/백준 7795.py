import sys
input = sys.stdin.readline

# a = 1 1 3 7 8
# b = 1 3 6

def cnt_pair(a, b):
    cnt = 0

    eatable = []

    i = 0
    l = 0
    for j in range(len(a)):
        if i >= len(b) or a[j] <= b[i]: # 먹잇감 아님
            cnt += l
            continue

        # 먹잇감임
     
        while i < len(b) and a[j] > b[i]:
            # print("a=", j, "b=", i)
            eatable.append(b[i])
            i += 1

        l = len(eatable)
        cnt += l

    
    return cnt

        

t = int(input().strip())

result = []

for _ in range(t):
    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    a.sort()

    b = list(map(int, input().split()))
    b.sort()


    result.append(cnt_pair(a, b))

for elem in result:
    print(elem)