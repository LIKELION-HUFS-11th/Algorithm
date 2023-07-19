# 입력
s = input()

# 함수들
def calc(final_formula):
    # ans
    ans = final_formula[0]

    # final_formula를 돌면서
    for i in range(1, len(final_formula)):
        # curr_mark
        curr_mark = final_formula[i]
        # curr_mark가 '+'이면
        if curr_mark == '+':
            # 더해주기
            ans += final_formula[i+1]
        # curr_mark가 '*'이면
        elif curr_mark == '*':
            # 곱해주기
            ans *= final_formula[i+1]
    
    # 반환
    return ans

# 설계
# 식을 세울 리스트
formula = []

# s를 탐색하면서
for i in range(len(s)):
    # 처음이면
    if i == 0:
        # 형변환하여 그냥 넣어주기
        formula.append(int(s[i]))

    # 이외에는 (처음이 아니면)
    else:
        # front, curr
        front, curr = formula[-1], int(s[i])
        
        # 둘 중 하나라도 0 또는 1이면
        if front <= 1 or curr <= 1:
            # 더하기가 유리
            formula.append('+')
            formula.append(curr)
        
        # 이외에는
        else:
            # 곱하기가 유리
            formula.append('*')
            formula.append(curr)

# 출력
# print(formula)
print(calc(formula))