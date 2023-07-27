class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        letter_logs = []
        num_logs = []
        num = "1234567890"
        
        #숫자로 된 로그 분리
        for i in logs :
            s = i.split()
            if s[1][0] in num :
                num_logs.append(i)
            else:
                 letter_logs.append(i)
        
        #문자로 된 로그 정렬하기
        sorted_letterlogs = sorted(letter_logs, key = lambda x : (x.split()[1:], x.split()[0]))
        #정렬한 문자로그 뒤애 숫자로그 붙이기(숫자로그는 입력순이므로 따로 정렬X)
        sorted_letterlogs.extend(num_logs)
            
        return sorted_letterlogs
        