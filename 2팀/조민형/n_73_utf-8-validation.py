class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            for j in range(i+1,i+size+1):
                if j >= len(data) or data[j] >> 6 != 0b10:
                    return False
            return True

        i=0
        while i < len(data):
            first = data[i]
            print(first)
            if (first>>3) == 0b11110 and check(3):
                i+=4
            elif (first>>4) == 0b1110 and check(2):
                i+=3
            elif(first>>5) == 0b110 and check(1):
                i+=2
            elif(first>>7) == 0:
                i+=1
            else:
                return False
        return True