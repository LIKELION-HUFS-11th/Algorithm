
#다시 풀어보자
#이건 민형이 코드

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []
        def dfs(elements):
            #만들어진 순열 추가
            if len(elements) == 0:
                result.append(prev_elements[:])

            #주어진 리스트 안에서 반복
            for i in elements:
                #리스트 복사
                next_elements = elements[:]
                next_elements.remove(i)
                #next_elemts에서는 지우면서 prev_elements에는 추가
                prev_elements.append(i)
                #재귀적으로 호출하면서 각 경우의 수를 모두 넣기
                #남은 리스트 안에서 다시 반복문을 돌면서 모든 경우의 수를 돌림
                dfs(next_elements)
                #다시 가장 바깥쪽에서 반복문이 정상적으로 돌아가도록 초기화
                prev_elements.pop()
        dfs(nums)
        return result