from typing import List
# 리스트의 요소 타입을 지정할 수 있게 해주는 것


def dailyTemper(T: List[int]) -> List[int]:
    answer = [0] * len(T)
    # 리스트를 초기화. 각각의 날짜에서 다음 따뜻한 날짜까지의 기간 저장
    stack = []
    # T의 인덱스 저장. 따뜻한 날짜까지의 기간이 1이 아닐 때, 해당 인덱스를 저장해줌
    for i, cur in enumerate(T):

        
    # i는 0부터 시작하는 인덱스값(=날짜), cur은 각 날짜의 온도
        while stack and cur > T[stack[-1]]:
    # 일단 stack이 비어있지 않을 때, 그리고 현재날짜의 온도가, 아직 처리되지 못한
    # 스택의 가장 위의 값보다 클 때!
            last = stack.pop()  #stack의 맨 위에 들어가있는 값
            answer[last] = i - last #그 차이를 넣어줌.
            
        stack.append(i) #스택의, 날짜는 계속 돌아간다.

    return answer
sample = dailyTemper([73, 74, 75, 71, 69, 72, 76, 73])

print(sample)