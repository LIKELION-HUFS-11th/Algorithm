class Solution:
    def find_longest_string(self, strings_list):
        return max(strings_list, key=len)

    # 슬라이싱을 통해 팰린드롬 확인
    def is_palindrome(self, s):
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        text = s
        result = []
        
        #해당사항이 없을 때 빠르게 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        # 첫번째 반복문 - 앞 글자 하나씩 지우기
        for i in range(len(text)):
            # 두번째 반복문 - 뒤 글자 하나씩 추가하면서 팰린드롬 확인
            for j in range(i + 1, len(text) + 1):
                substring = text[i:j]
                # 팰린드롬일 경우 결과에 추가
                if self.is_palindrome(substring):
                    result.append(substring)

        # 들어간 팰린드롬 중에 가장 문자열의 길이가 긴 팰린드롬 리턴
        longest = self.find_longest_string(result)

        return longest
