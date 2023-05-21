def zip(cut):
    
    if len(cut) == 1: return 1
    
    zip_s = ""
    temp = cut[0]
    cnt = 1
    
    for i in range(1, len(cut)):
        if cut[i] == temp:
            if i == len(cut)-1:
                zip_s += str(cnt+1) + temp
            else:
                cnt += 1
        else:
            if cnt > 1:
                zip_s += str(cnt) + temp
            else:
                zip_s += temp
            cnt = 1
            temp = cut[i]
                
            if i == len(cut)-1:
                zip_s += cut[i]
    
    return len(zip_s)


def solution(s):
    
    length = len(s)
    zip_length = [len(s)]
    
    for i in range(1, (length//2)+1):
        cut = []
        cnt = 0
        for _ in range((length//i)):
            cut.append(s[cnt:cnt+i])
            cnt += i
            
        if cnt <= length-1:
            cut.append(s[cnt:])
        
        zip_length.append(zip(cut))
    
    
    answer = min(zip_length)
    
    return answer