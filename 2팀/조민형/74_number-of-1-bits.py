class Solution:
    def hammingWeight(self, n: int) -> int:
        tostr = str(bin(n))
        return tostr.count("1")