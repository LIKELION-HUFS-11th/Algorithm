class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        stones_dict = {}

        for i in stones:
            if i not in stones_dict:
                stones_dict[i] = 1
            else:
                stones_dict[i] += 1

        for j in jewels:
            if j not in stones_dict:
                pass
            else:
                count = count + stones_dict[j] 
        
        return count
        