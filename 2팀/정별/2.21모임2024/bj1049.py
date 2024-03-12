n, m = map(int, input().split())
nPrice = []
for _ in range(m):
    x, y = map(int, input().split())
    nPrice.append(x)
    nPrice.append(y)

sys = 10000
cnt = 0
if n < 6: #기타줄이 6개 미만으로 끊어진다면
    for i in range(1, len(nPrice), 2):
        if nPrice[i] < sys:
            sys = nPrice[i]
    cnt = n *sys
    
elif n == 6:
    for i in range(0, len(nPrice), 2):
        if nPrice[i] < sys:
            sys = nPrice[i]
    cnt = sys
else:

    for i in range(0, len(nPrice), 2):
        if nPrice[i] < sys:
            sys = nPrice[i]
    cnt *= (n//6)
    
    ysy = 10000
    for i in range(1, len(nPrice), 2):
        if nPrice[i] < ysy:
            ysy = nPrice[i]
    cnt *= (n%6)

print(cnt)