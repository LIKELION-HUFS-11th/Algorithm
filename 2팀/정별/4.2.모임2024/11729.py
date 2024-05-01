N = int(input())
cnt=0
nList =[]

def hanoi(n, start, target, aux): #target은 기둥3, aux는 기둥2
    global cnt
    global nList
    
    if n == 1:
        nList.append((start, target))
        cnt+=1
        return
    # n-1개를 aux로 이동
    hanoi(n-1, start, aux, target) #가장 큰 원판 제외 나머지 모든 애들을, 기둥2로 옮김
    
    # 가장 큰 원판을 target으로 이동
    nList.append((start, target))
    cnt+=1 #가장 큰 원판 옮길 때 카운트
    
    # aux에 있는 n-1개 원판들을 target으로 이동
    hanoi(n-1, aux, target, start)

# 3개의 원판을 가지고 1번 기둥에서 3번 기둥으로 이동하는 예시

hanoi(N, 1, 3, 2)
print(cnt)
for elem in nList:
    print(elem[0], end=' ')
    print(elem[1])

# from string import ascii_lowercase

# alphabet = list(ascii_lowercase) #a b c.. 순서대로 크기가 커지는 것임

# stack1 =[] #장대 1
# stack2 =[] #장대 2
# stack3 =[] #장대 3

# for elem in alphabet[:N]:
#     stack1.append(elem)
# stack1.reverse() #큰 순서대로 먼저 아래에 깔려있음.

# nS1_len = len(stack1)

# while len(stack3)<= nS1_len: #stack3이 다 찰 때까지.

#start, target, aux 순서 왔다갔다 번갈아 하면서 재귀