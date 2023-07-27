#입력
x = int(input())

#d[i] = i가 1이 되는 데 필요한 연산횟수의 최솟값
d = [0] * 30001

for i in range(2,x+1):
    d[i] = d[i-1] + 1
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)

    if i % 5 ==0:
        d[i] = min(d[i], d[i//5]+1)

#출력
print(d[x])