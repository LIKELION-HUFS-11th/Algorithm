import sys

T = int(input())
answer = 0

# idx 번째 포지션에 적합한 선수를 고르고,
# 다음 포지션을 재귀적으로 탐색

def select(idx, mat, pos, visit, value):
    # 모든 선수들을 다 고를 수 있는 경우에만 최대값 갱신
    if idx == 11:
        global answer
        if value > answer:
            answer = value
        return
    
    # 해당 포지션에 적합한 모든 선수들을 탐색
    for candidate in pos[idx]:
        #방문했으면 제외
        if visit[candidate]: 
            continue
        visit[candidate] = True
        
        # value 에 해당 선수의, 해당 포지션 능력치를 더해주면서 다음 포지션 재귀호출
        select(idx+1, mat, pos, visit, value+mat[candidate][idx]) #계속 value 더해주다가, 막판에 answer로 바꿔줌.
        
        visit[candidate] = False

for _ in range(T):
    mat = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]
    
    # 각 포지션마다 적합한 선수들의 목록
    pos = [[] for _ in range(11)]
    
    for i, player in enumerate(mat): #i는 선수 고유번호, player는 해당 선수의 모든 포지션에서의 능력 리스트
        for idx, val in enumerate(player): #idx는 포지션 고유번호, val은 그 포지션에서 선수 역량
            if val != 0:
                pos[idx].append(i) #능력치 있다면 일단 담기. 
                #->이렇게 pos 안을 채우고 나서 함수 돌림.
                
    # 포지션을 차례대로 선택하는 백트래킹
    
    select(0, mat, pos, [False for _ in range(11)], 0) #방문여부 처음엔 False
    print(answer)
    
    #정답 값 초기화
    answer = 0