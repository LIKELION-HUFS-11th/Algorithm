def solution(N, stages):
    
    # fail_ratios
    fail_ratios = []
    
    # user_num
    user_num = len(stages)
    
    for i in range(1, N+1):
        cnt = stages.count(i)
        
        if cnt==0:
            fail_ratio = 0
        else:
            fail_ratio = cnt / user_num
        
        fail_ratios.append((i, fail_ratio))
        user_num -= cnt
    
    fail_ratios.sort(key=lambda x:x[1], reverse=True)
    
    ans = []
    for fail_ratio in fail_ratios:
        ans.append(fail_ratio[0])
    return ans