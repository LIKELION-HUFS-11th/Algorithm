        # def find_max_str(blank, char, index):
        #     global end #전역변수: 양쪽에 모두 붙여야 함
        #     if index > len(s)-1:
        #         print("1 and ", end)
        #         return

        #     if s[index] == char:
        #         end = index
        #         print("4 wow")
        #         find_max_str(blank, char, index+1)
        #     else:
        #         if blank > 0: #바꿀 수 있는 기회가 남아있음
        #             end = index
        #             print("3 wow")
        #             find_max_str(blank-1, char, index+1)
        #         elif blank == 0: #최대길이에 도달
        #             print("2 and ", end)
        #             return