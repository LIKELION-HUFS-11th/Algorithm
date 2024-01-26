class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        #Sol 1
        def check_n_bytes(byte, index):
            global cnt
            cnt, i = 1, 1 #이미 byte[0] = 1인건 확인됐음
            while i < len(byte) and byte[i] == "1": #몇 바이트 문자인지 검사
                cnt += 1
                i += 1

            if cnt > 4: #조건 1) 4바이트 초과 시 false
                return False

            i = index + 1
            satisfied = False
            #cnt-1개 바이트들을 검사
            while index + cnt <= len(data) and i < index + cnt: #조건2) 바이트들이 부족하면 false
                if data[i][0] == "1" and data[i][1] == "0":
                    satisfied = True
                    i += 1
                else:
                    satisfied = False #조건 3) 10 조건 안 맞을시 false
                    break
            
            return satisfied


        for i in range(len(data)):
            data[i] = bin(data[i])[2:]
            if len(data[i]) < 8:
                data[i] = "0" * (8-len(data[i])) + data[i]
            print(data[i])


        # for i in range(len(data)):
        i = 0
        while i < len(data):
            byte = data[i]

            if byte[0] == "1": #2~4byte 문자
                if check_n_bytes(byte, i) == True: #("110xxxxx", 0)
                    i += cnt #다음 문자로 이동
                else: #하나라도 조건에 맞지 않으면 false
                    return False

            else: #1byte 문자
                i += 1
        
        return True

        ##########################################
        #Sol 2
        def check(size):
            for i in range(start + 1, start + size + 1): #n-1(=size)바이트의 수들을 체크
                if i >= len(data) or (data[i] >> 6) != 0b10: #조건 2, 3 체크
                    return False
            return True
        
        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and check(3): # >>N : 왼쪽으로 N번 시프팅 -> 11110xxx 수를 >>3 하면 11110이 됨 -> 4바이트 수
                start += 4
            elif (first >> 4) == 0b1110 and check(2): #3바이트 수
                start += 3
            elif (first >> 5) == 0b110 and check(1): #2바이트 수
                start += 2
            elif (first >> 7) == 0: #1바이트 수
                start += 1
            else:
                return False
        return True

        
    