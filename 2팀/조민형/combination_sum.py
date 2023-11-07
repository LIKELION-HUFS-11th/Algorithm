class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(templist, start, path):
            if sum(path) == target:
                result.append(path[:])
                return
            if sum(path) > target:
                return
            for i in range(start, len(templist)):
                path.append(templist[i])
                dfs(templist, i, path)
                path.pop()

        result = []
        dfs(candidates, 0, [])
        return result
