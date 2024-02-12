class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """


        def compute(left, right, op):
            res = [] 
            for l in left:
                for r in right:
                    res.append(eval(str(l) + op + str(r))) #문자열 형태로 들어온 식의 결과값 반환
            return res

        if expression.isdigit(): #바닥조건 : 문자열의 모든 문자가 숫자로만 이루어졌으면 True
            return [int(expression)]

        results = []

        for index, value in enumerate(expression):
            if value in "-+*": #숫자를 기준으로 분할하면 복잡해짐 - 연산자 기준으로 분할!
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])

                results.extend(compute(left, right, value)) #compute의 반환 리스트가 여러 원소로 이루어져 있을 수 있음 -> 언제? 
        
        return results

            


        