def trimmed_u(u):
    # n (u의 길이)
    n = len(u)
    
    # 길이가 2 이하이면
    if n <= 2:
        # 빈 문자열 반환
        return ''
    
    # 길이가 3 이상이면
    # temp
    temp = ''
    for i in range(1, n-1):
        # 반대로 추가
        if u[i] == '(':
            temp += ')'
        else:
            temp += '('
    
    # 반환
    return temp
    
def get_idx(p):
    
    # left_cnt, right_cnt
    left_cnt, right_cnt = 0, 0

    for i in range(len(p)+1):
        # 균형이 잡히면
        if left_cnt != 0 and right_cnt != 0 and left_cnt == right_cnt:
            # 반환
            return i
        
        # 왼쪽 괄호이면
        if p[i] == '(':
            left_cnt += 1
        
        # 오른 쪽 괄호이면
        else:
            right_cnt += 1
    
def is_right(p):
    
    # stack
    stack = []
    
    # 검사
    for i in p:
        # '('일 때
        if i == '(':
            # stack에 push
            stack.append(i)
        # ')'일 때
        elif i == ')':
            # 스택이 비어있으면
            if not stack:
                # 실패
                return False
            # 스택이 안비어있으면
            # 스택의 top이 '('이면
            if stack[-1] == '(':
                # pop 처리
                stack.pop()
    
    # 스택이 비어있는지 반환
    return not stack

def calc(p):
    
    # 비어있거나 올바른 문자열이면
    if not p or is_right(p):
        # 그대로 반환
        return p
    
    # 문자열을 u,v로 나눠 줄 idx 구하기
    idx = get_idx(p)
    
    # u, v
    u, v = p[:idx], p[idx:]

    # u가 올바른 문자열이면
    if is_right(u):
        # v에 대해 calc를 수행 해 u에 이어붙여 반환
        return u + calc(v)
    
    # u가 올바른 괄호 문자열이 아니라면
    else:
        temp = '('
        temp += calc(v)
        temp += ')'
        temp += trimmed_u(u)
        return temp

def solution(p):
    return calc(p)