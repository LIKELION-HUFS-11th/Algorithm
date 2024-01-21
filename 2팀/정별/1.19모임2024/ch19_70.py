class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        answer = {} #dict 형태로 저장하고 비교.
        #key는 숫자 value는 개수
        
        for i in nums: 
            if i in answer:
                answer[i] += 1
            else:
                answer[i] = 1
        
        for k, v in answer.items(): #k는 key, v는 value
            if v == 1: # 다시 for문 돌려서 value 1개인거 추출
                return k