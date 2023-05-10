def get_len(curr_list):
    
    ans_list = []
    
    cnt = 1
    
    for i in range(len(curr_list) - 1):
        if curr_list[i] == curr_list[i+1]:
            cnt += 1
        else:
            if cnt > 1:
                ans_list.append(str(cnt))
            
            ans_list.append(curr_list[i])
            cnt = 1
    
    if cnt > 1:
        ans_list.append(str(cnt))
    
    ans_list.append(curr_list[-1])
    
    total_length = 0

    for s in ans_list:
        total_length += len(s)

    return total_length
            

def simulate(p, s):
    
    s_list = []
    
    i = 0
    for _ in range(len(s) // p + 1):
        s_list.append(s[i:i+p])
        i += p
        
    return get_len(s_list)
        

def solution(s):
    # shortest
    shortest = len(s)
    
    # 완전 탐색 시작
    for i in range(1, len(s) // 2 + 1):
        # shortest 갱신
        shortest = min(shortest, simulate(i, s))
    
    return shortest