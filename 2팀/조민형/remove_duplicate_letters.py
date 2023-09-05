class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {}  # 문자의 마지막 등장 위치를 저장하는 딕셔너리
        for i, char in enumerate(s):
            last_occurrence[char] = i

        stack = []
        seen = set()  # 이미 스택에 추가된 문자를 추적하는 집합

        for i, char in enumerate(s):
            if char in seen:
                continue

            while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                # 스택의 맨 위 문자가 현재 문자보다 사전순이 크고
                # 그 문자의 마지막 등장 위치가 현재 위치 이후에 있다면 스택에서 제거
                seen.discard(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)
