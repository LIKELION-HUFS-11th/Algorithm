class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        S = [0] * (n+1) #index 0은 사용 안 함

        for i in range(1, n+1):
            if i < 3:
                S[i] = i #S[1] = 1, S[2] = 2
            else:
                S[i] = S[i-1] + S[i-2]

        return S[n]