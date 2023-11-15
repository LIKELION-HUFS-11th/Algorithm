class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numlist = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        def dfs(index, path):
            if len(path) == len(digits): #바닥까지 내려갔다면 문자열 저장
                result.append(path)
                return
            
            for i in range(index, len(digits)): #i의 증가 = digits간 이동
                for j in numlist[digits[i]]: #j의 증가 : digit내 문자 하나씩 봄
                    dfs(i+1, path+j) #path에 문자를 하나씩 추가하며 반환
        #순환함수를 매번 호출할때마다 변수값을 어떻게 조정하나 했는데 매개변수를 활용해 이렇게 하면 되더라!         

        # digits = "23" 예시에서
        # dfs(0,"" > 1,"a" > 2,"ad" > 2,"ae" > 2,"af" > 3,)
        # path = a -> ad / ae / af / b -> bd / be / bf / c -> cd / ce / cf

        if not digits: #공백 입력시 예외처리
            return []
        
        result = []
        dfs(0, "")

        return result


        