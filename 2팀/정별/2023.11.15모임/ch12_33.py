class Solution:
    def letterCombinations(self, inp:str) :
        ic = {
                    '2':['a', 'b', 'c'],
                    '3':['d', 'e','f'],
                    '4':['g', 'h', 'i'],
                    '5':['j', 'k', 'l'],
                    '6':['m', 'n', 'o'],
                    '7':['p', 'q', 'r', 's'],
                    '8':['t', 'u', 'v'],
                    '9':['w', 'x', 'y', 'z']
                }

        def dfs(idx, path):
            if len(path) == len(inp):
                result.append(path)
                return
            
            if idx < len(inp):
                for j in ic[inp[idx]]:
                    dfs(idx + 1, path + j)
        if not inp:
            return []
        
        result = []
        dfs(0, '')
        
        return result

if __name__ == '__main__':
    s = Solution()
    ans = s.letterCombinations('789')
    print(ans)

# for i in range(idx, len(inp)):
#     for j in ic[inp[i]]:
#         dfs(i+1, path + j)


#elem은 각 숫자들임
# ans = []
# def comb(o, elem, results):
#     for e in ic[elem[o]]:
#         results.append(e)
#     return results

# for i in range(len(inp)):
#     print(comb(i, inp, ans))


# for i in range(len(inp)):
#     comb()

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Input: digits = "2"
# Output: ["a","b","c"]