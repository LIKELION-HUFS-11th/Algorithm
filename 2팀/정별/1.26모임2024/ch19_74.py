def hammingWeight(self, n):
    return bin(n).count('1')

#모두 0으로 구성된 비트와의 해밍 거리
#bin(A XOR B)
#bin(n ^ 00000000000000000000000000000000)