class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # sol1 - O(n)
        F = [0] * (n+1)
        
        for i in range(0, n+1):
            if i <= 1:
                F[i] = i
            else:
                F[i] = F[i-1] + F[i-2]

        return F[n]

        # sol2) 분할정복방법 - 오래 걸림 (지수시간)
        # if n <= 1:
        #     return n
        # return self.fib(n - 1) + self.fib(n - 2)
