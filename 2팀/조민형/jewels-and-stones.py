class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_dict = {}

        for j in jewels:
            jewels_dict[j] = 1

        for i in stones:
            if i in jewels_dict:
                count += 1
        
        return count
        