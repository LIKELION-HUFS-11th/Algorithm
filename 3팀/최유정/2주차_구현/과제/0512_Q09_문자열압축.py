def solution(s):
    answer = 1
    min_len = float('inf')
    c = len(s)//2
    result = ""
    if len(s) == 1:
        return 1
    for i in range(1, c+1):
        for a in range(0, len(s), i):
            if s[a:a+i] == s[a+i:a+2*i]:
                answer+=1
            else:
                if answer == 1:
                    result += s[a:a+i]
                else:
                    result += (str(answer)+s[a:a+i])
                answer = 1
        if min_len > len(result):
            min_len = len(result)
            min_result = result
        result = ""
    return min_len


s = "a"
print(solution(s))