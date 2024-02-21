
#이렇게 하니까 시간초과
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         elif n ==2:
#             return 2
#         else:
#             return self.climbStairs(n-1) + self.climbStairs(n-2)
    

class Solution:
    dp = collections.defaultdict(int)
    
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        
        if self.dp[n]:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return self.dp[n]