
class Solution:
    def combinationSum(self, candidates, target=0) :
        result = []

        def dfs(csum, index, path): #csum은 조합되어야할 target 값임
            if csum < 0:
                return
            if csum == 0: #구해야할 csum과 여기까지의 조합의 합이 일치하는 순간임
                result.append(path)
                return

            for i in range(index, len(candidates)): #그래프상 1층의 노드들을 순회
                dfs(csum - candidates[i], i, path + [candidates[i]]) #그 아래층의 노드들을 순회
        
        dfs(target, 0, [])
        
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))

  
# index를 제외하면;
# print(s.combinationSum([2, 3, 6, 7], 7))
# 출력이 [[2, 2, 3], [2, 3, 2], [3, 2, 2], [7]] 로 나옴.
# 즉, 그래프상 내가 탐색했던 길들은 무시할 수 있음