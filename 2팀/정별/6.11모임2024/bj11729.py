k = int(input())

cnt = 0
nList = [] #쌍으로 이동 궤도 담아두기

def hanoi(n, pil1, pil2, pil3): #모든 판의 이동은 pil1-> pil3 방향으로 고정
    global cnt
    
    if n == 1:
        nList.append([pil1, pil3]) #pil2->pil3으로 가는건 최종 작업으로 고려하지 않음
        cnt+=1
        return
    
    #pil1에 있는 1~n-1의 원판들을 일단 pil2로 옮기는 것임
    hanoi(n-1, pil1, pil3, pil2)
    #n-1이하의 원판들이 다 치워졌으면, 가장 큰 n원판 옮김
    nList.append([pil1, pil3]) #가장 큰 원판인 현재의 n원판을 타겟으로 옮김
    cnt +=1
    
    hanoi(n-1, pil2, pil1, pil3)

hanoi(k, 1, 2, 3)
print(cnt)

for i in range(cnt):
    for j in range(2):
        print(nList[i][j], end=' ')
    print()
    

