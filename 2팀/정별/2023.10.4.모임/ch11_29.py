class Solution:
    def JInS(jewels: str, stones: str) -> int:
        J = jewels
        S = stones
        
        freqs = {}

        for char in S:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1
        
        cnt = 0
        for char in J:
            if char in freqs:
                cnt += freqs[char]

        return cnt
    
print(Solution.JInS('aAb', 'bAAac'))
