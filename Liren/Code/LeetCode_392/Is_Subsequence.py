class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for index in range(len(s)):
            char = s[index]
            if len(t) == 0:
                return False
            if char in t:
                t = t[t.index(char)+1:]
            else:
                return False
        return True
