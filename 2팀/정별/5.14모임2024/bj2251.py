import sys

A, B, C = map(int, sys.stdin.readline().split()) #각 컵의 전체 부피

nAns =[] #정답 담을 리스트
nVisited = [0] * 201 #최댓값 200. c의 출력여부 확인
nCheck = [[[0] * 201 for _ in range(201)] for _ in range(201)]
 #3차원 상에서 a b c 상태가 과거 존재 했었는지 확인
 
# nCheck = [[[0] * 201]*201]*201
# nCheck[A][B][C] = True  #이거하면 바로 종료.
def bfs(a, b, c): #매개변수 a,b,c는 A,B,C 컵에 남아있는 물의양임
    if nCheck[a][b][c]: #이미 계산했던 상태라면 복귀
        return

    nCheck[a][b][c] = True
    
    if a == 0 and nVisited[c] == 0: #답 도출 조건. A가 비어있으면.
        nVisited[c] = True
        nAns.append(c)
    
    nCapa, nCapb, nCapc = A-a, B-b, C-c #전체 부피에서 현재 들어있는 애들을 뺀 나머지 용량
    
    #보내는쪽은 자기가 비워야하니 max, 받는쪽은 다 안차도 유지 가능하니 min
    bfs(a + min(nCapa, c) , b, max(0, c-nCapa))#c->a a에는 최소로 더해야함. #c는 다주거나, a full로 채우거나
    bfs(a, b+ min(nCapb, c), max(0, c-nCapb) )#c->b 위와 동일.
                #nCapb 선택이면, b가 full임.
                             #0과 비교를 해야, 계속 돌면서 c를 줄여줌
                
    bfs(max(0, a-nCapb) , b+ min(nCapb, a) ,c) #a->b
    bfs(max(0, a-nCapc), b ,c+min(nCapc, a))#a->c
    
    bfs(a, max(0, b-nCapc), c+min(nCapc, b))#b->c
    bfs(a+min(b, nCapa), max(0, b-nCapa),c)#b->a

bfs(0, 0, C) #처음 상태
# print(nVisited)
# print(nCheck)
# print(nAns)
nAns.sort() #오름차순 정렬
for elem in nAns:
    print(elem, end=' ')
    

# nC = 0 #남아있는 c용량
# nArray = []
# while True:
    
#     if c>= b and c>=a:
        
#         if b>= a:
#             nC += c-b-a
#         else: # b<a
#             nC = c-a+(a-b) #a 먼저 꽉 채우고, b

#     nC.append(nArray)


#올바른 3차원 배열 설정 방법
# nCheck = [[[0] * 201]*201]*201
# 이 방법은 3차원 리스트를 만들되, 내부 리스트가 모두 같은 객체로 참조되기 때문에 문제를 일으킬 수 있습니다. 
# 즉, nCheck 리스트 내의 모든 위치가 동일한 객체를 참조하게 됩니다. 이렇게 되면 
# 하나의 위치를 수정하면 해당 위치와 같은 인덱스를 가진 다른 위치도 같이 수정될 수 있습니다.

# 이러한 문제를 해결하기 위해서는 내부 리스트를 각각의 독립적인 객체로 초기화해야 합니다. 그래서 제가 제안한 변경은 다음과 같이 각 내부 리스트를 독립적으로 초기화하여 3차원 리스트를 만드는 것입니다:

# nCheck = [[[0] * 201 for _ in range(201)] for _ in range(201)]
# 이 변경으로 인해 nCheck 리스트 내의 각 위치는 서로 독립적인 객체를 참조하게 되어 중복된 상태를 올바르게 체크할 수 있게 됩니다. 이는 코드의 정확성을 보장하는데 중요한 요소입니다. 따라서 이 변경을 통해 코드의 정확성이 향상되었고, 올바른 답을 반환할 수 있었습니다.





