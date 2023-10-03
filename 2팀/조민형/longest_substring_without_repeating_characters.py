class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = {}
        result = {}

        i = 0
        j = 0
        while i < len(s):
            if s[i] not in sub:
                result[s[j:i+1]] = len(s[j:i+1])
                sub[s[i]] = 1
            elif s[i] in sub:
                sub.clear()
                j = i
                result[s[j:i+1]] = len(s[j:i+1])
                sub[s[i]] = 1
            i += 1

        maxcount = 0
        longlist = list(result.keys())
        print(longlist)
        for j in longlist:
            if result[j] > maxcount:
                maxcount = result[j]
        return maxcount
