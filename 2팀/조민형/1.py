class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. 유효한 팰린드롬
        numandstring = "qwertyuiopasdfghjklzxcvbnm1234567890"
        text = s.lower()
        text_extraction = []

        # 문자와 숫자가 안에 들어있으면 리스트에 추가
        for i in text:
            if i in numandstring:
                text_extraction.append(i)

        realtext = "".join(text_extraction)

        istrue = True
        if realtext[::] != text_extraction[::-1]:
            istrue = False

        return istrue
