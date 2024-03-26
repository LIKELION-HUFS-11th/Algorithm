# 133ms
# g= [1,2,3]
# s= [1,1]

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()

        cnt = 0 #최대 줄 수 있는 아이들이자 g 인덱스값들을  돌 포인터.
        j = 0 # s를 돌 포인터 = 모든 쿠키들 돌 포인터

        while len(s) > j and len(g) > cnt: #둘다 전부 종료될 때까지 진행
            if s[j] >= g[cnt]:
                cnt += 1
            j += 1
            # if elem in g:
            #     cnt+= 1
            #     g.remove(elem)
        return cnt