
class Solution:
    def Longest(self, s: str) -> int:
        
        h = {}
        maxi = 0
        arrive = 0
        
        for i, elem in enumerate(list(s)):
            #문자열 중복됐을시 arrive 갱신
            if elem in h:
                #나랑 같은 elem의 가장 최신 갱신된 인덱스값. 에서 한칸 이동
                arrive = max(arrive, h[elem] + 1)
                
            
            #해시맵에 업데이트
            h[elem] = i

            cur_len = i - arrive + 1
            maxi = max(maxi, cur_len)
            
        print(maxi)
        
obj = Solution()
obj.Longest("abcabcbb")
obj.Longest("bbbb")
obj.Longest("pwwkew")
    