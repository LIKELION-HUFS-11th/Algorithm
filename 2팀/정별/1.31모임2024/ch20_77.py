
# # test1
# s= "ABAB"
# k= 2

# # test2
# s = "AABABBA"
# k = 1

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

    #dict으로 key는 해당 문자, value는 문자의 반복 개수
    dic = {}
    for elem in s:
        dic[elem] = dic.get(elem, 0) +1

    dic = list(dic.items())
    
    left = right = 0

    max = 0
    max_char_n = #dic돌면서 최대 문자의 value 찾아야함

    for right in range(1, len(s) + 1):
        dic[s[right - 1]] += 1
        

        if right - left - max_char_n > k:
            dic[s[left]] -= 1
            left += 1
    return right - left
