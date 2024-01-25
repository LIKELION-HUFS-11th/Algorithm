class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        need = Counter(t)
        missing = len(t)
        left = start= end = 0
        for right, char in enumerate(s,1):
            missing -=need[char]>0
            need[char]-=1

            if missing ==0:
                while left < right and need[s[left]] <0:
                    need[s[left]] +=1
                    left +=1
                
                if not end or right - left <= end-start:
                    start,end = left,right
                    need[s[left]] +=1
                    missing +=1
                    left +=1
        return s[start:end]



# from collections import Counter

# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         def check_letter(s, t):
#             s_dict = Counter(s)
#             # t의 모든 문자가 s에 포함되어 있는지 확인
#             for char in t:
#                 if s_dict[char] - t_dict[char] < 0:
#                     return False
#             return True
        
#         t_dict = Counter(t)
#         i = len(t)-1
#         j=0
#         result = ""
#         if len(t)==len(s) and sorted(s) == sorted(t):
#             return s
#         elif len(t)==1 and t in s:
#             return t
#         elif len(t)>len(s):
#             return ""
#         # len(s)=3 i=1 j=0
#         while i<=len(s):
#             if check_letter(s[j:i],t_dict) == True:
#                 if result and len(result) > len(s[j:i]):
#                     result = s[j:i]
#                     j+=1
#                     continue
#                 elif result:
#                     j+=1
#                     continue
#                 result = s[j:i]
#                 j+=1
#             else:
#                 i+=1
#         if result:
#             return result
#         else: return ""
    