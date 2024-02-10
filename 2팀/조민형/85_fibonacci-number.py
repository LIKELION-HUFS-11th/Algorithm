class Solution:
    def fib(self, n: int) -> int:
        def fib_cal(n):
            if n<=1:
                return n
            fb=[0] * (n+2)
            fb[0] = 0
            fb[1]=1
            for i in range(2,n+2):
                fb[i] = fb[i-1] + fb[i-2]
            return fb[n-1] + fb[n-2]
                
        return fib_cal(n)
    
print(Solution.fib(Solution,n=10))