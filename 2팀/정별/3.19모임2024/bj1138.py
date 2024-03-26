import sys

n = int(input())
nPeople = list(map(int, sys.stdin.readline().split()))

res=[0]*n

dic ={}
for i, elem in enumerate(nPeople):
    dic[i+1] = dic.get(i+1, elem)
# dic = sorted(dic.keys(), reverse=True) #큰 수부터 할 수 있게 뒤집어주기


for key in dic:
    if key == 1: #1번이 들어갈 자리 고정
        res[dic[key]] = key

    for i in range(len(res)):
        if res[i] != 1 and i>= dic[key]:
            res[i] = key
            break
        
    # res.index(1)

print(res)


