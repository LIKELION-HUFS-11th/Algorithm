#44ms
n, k = map(int, input().split())

nCoins =[]

for _ in range(n):
    nElem = int(input())
    if nElem <= k: #여기서 = 안붙여서 디버깅하느라 시간..,
        nCoins.append(nElem)


cnt = 0 #답

for j in range(len(nCoins), 0, -1):

    if k == 0:
        break
    
    if k % nCoins[j-1] == 0: #딱 떨어지면
        cnt += (k//nCoins[j-1])
        break
    
    if k <nCoins[j-1]:
        continue
    # elif k == nCoins[j-1]:
    #     cnt +=1
    #     break
    else:
        cnt += k//nCoins[j-1]
        k %= nCoins[j-1]

print(cnt)
