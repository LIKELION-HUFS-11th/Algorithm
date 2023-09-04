class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_list = []

        for i in s:
            if i == '(':
                parenthesis_list.append(i)

            elif i == '[':
                parenthesis_list.append(i)

            elif i == '{':
                parenthesis_list.append(i)

            elif i == ')':
                if '(' in parenthesis_list and parenthesis_list[-1] == '(':
                    parenthesis_list.pop()
                else:
                    parenthesis_list.append(i)
            elif i == ']':
                if '[' in parenthesis_list and parenthesis_list[-1] == '[':
                    parenthesis_list.pop()
                else:
                    parenthesis_list.append(i)
            elif i == '}':
                if '{' in parenthesis_list and parenthesis_list[-1] == '{':
                    parenthesis_list.pop()
                else:
                    parenthesis_list.append(i)

        if len(parenthesis_list) == 0:
            return True
        elif len(parenthesis_list) > 0:
            return False
