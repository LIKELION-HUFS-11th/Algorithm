class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        
        hashtable = {} #딕셔너리형
        cnt = 0

        for stone in stones: #해시 테이블 생성 - 현재 있는 돌 개수
            if stone in hashtable.keys():
                hashtable[stone] += 1
            else:
                hashtable[stone] = 1
        
        # {'a':1, 'A':2, 'b':4}


        for jewel in jewels: #해시테이블과 대조
            if jewel in hashtable.keys():
                cnt += hashtable[jewel]
        
        return cnt