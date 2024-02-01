#빠른거
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result = 0
        s.sort()
        g.sort()
        
        j = 0
        i=0
        while i<len(s) and j<len(g):
            if s[i] >= g[j]:
                j+=1
                i+=1
                result +=1
            else: i+=1
                
        return result
                
            
# class Solution:
#     def findContentChildren(self, g: List[int], s: List[int]) -> int:
#         result = 0
#         s.sort()
#         g.sort()
        
#         for j in range(len(g)):
#             for i in range(len(s)):
#                 if s[i] > g[j] :
#                     del s[i]
#                     result +=1
#                     break
#                 elif s[i] == g[j]:
#                     del s[i]
#                     result+=1
#                     break
#                 else: continue
#         return result
                
            