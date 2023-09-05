class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_list = []  # 괄호 문자를 저장할 스택

        for i in s:
            if i == '(':  # 열린 괄호인 경우
                parenthesis_list.append(i)  # 스택에 추가

            elif i == '[':  # 열린 대괄호인 경우
                parenthesis_list.append(i)  # 스택에 추가

            elif i == '{':  # 열린 중괄호인 경우
                parenthesis_list.append(i)  # 스택에 추가

            elif i == ')':  # 닫힌 괄호인 경우
                # 스택이 비어있지 않고 가장 최근 열린 괄호와 짝인 경우
                if '(' in parenthesis_list and parenthesis_list[-1] == '(':
                    parenthesis_list.pop()  # 짝을 이룬 열린 괄호 제거
                else:
                    parenthesis_list.append(i)  # 스택에 추가 (짝이 없는 경우)

            elif i == ']':  # 닫힌 대괄호인 경우
                # 스택이 비어있지 않고 가장 최근 열린 대괄호와 짝인 경우
                if '[' in parenthesis_list and parenthesis_list[-1] == '[':
                    parenthesis_list.pop()  # 짝을 이룬 열린 대괄호 제거
                else:
                    parenthesis_list.append(i)  # 스택에 추가 (짝이 없는 경우)

            elif i == '}':  # 닫힌 중괄호인 경우
                # 스택이 비어있지 않고 가장 최근 열린 중괄호와 짝인 경우
                if '{' in parenthesis_list and parenthesis_list[-1] == '{':
                    parenthesis_list.pop()  # 짝을 이룬 열린 중괄호 제거
                else:
                    parenthesis_list.append(i)  # 스택에 추가 (짝이 없는 경우)

        if len(parenthesis_list) == 0:
            return True  # 스택이 비어있으면 유효한 괄호 문자열
        elif len(parenthesis_list) > 0:
            return False  # 스택에 여전히 괄호 문자가 남아있으면 유효하지 않은 괄호 문자열
