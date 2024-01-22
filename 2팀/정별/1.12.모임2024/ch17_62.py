#풀이1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        nSorts = sorted(s)
        nSortt = sorted(t)
        if nSorts == nSortt:
            return True
        else:
            return False

#풀이2 set
s = 'anagram'
t = 'nagaram'
print(set(s)==set(t))