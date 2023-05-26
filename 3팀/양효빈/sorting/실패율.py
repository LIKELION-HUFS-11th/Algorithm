
def solution(N, stages):
    
    stage_arr = []
    for i in range(1, N+1):
        fail = stages.count(i)
        
        cnt = 0
        for j in range(len(stages)):
            if stages[j] >= i : cnt += 1
            
        stage_arr.append([fail/cnt, i])
    
    stage_arr.sort(key=lambda x: x[0], reverse=True)

    answer = []
    for s in stage_arr:
        answer.append(s[1])

    return answer

