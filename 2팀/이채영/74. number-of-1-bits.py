class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        #모두 0으로 구성된 비트와의 해밍 거리
        #bin(A XOR B)
        #bin(n ^ 00000000000000000000000000000000)

        return bin(n).count('1') 
        