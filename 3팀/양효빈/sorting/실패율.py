def same_per(N, stage_arr):
    answer = []
    temp = []
    
    pos = 0
    arr = []
    for i in range(1, N):
        if stage_arr[pos] == stage_arr[i]:
            arr.append(stage_arr[i][1])
        else:
            if len(arr) > 0:
                temp.append(arr)
                arr = []
            else:
                temp.append([stage_arr[pos][1]])
            pos = i
            
    
    for t in temp:
        t.sort()
        
    for t in temp:
        for stage in t:
            answer.append(stage)

    return answer





def solution(N, stages):
    
    stage_arr = []
    for i in range(1, N+1):
        fail = stages.count(i)
        
        cnt = 0
        for j in range(len(stages)):
            if stages[j] >= i : cnt += 1
            
        stage_arr.append([fail/cnt, i])
    
    stage_arr.sort(key=lambda x: x[0])
    
    answer = same_per(N, stage_arr)
    return answer