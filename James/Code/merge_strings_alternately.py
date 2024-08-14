class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lew1 = len(word1)
        lew2 = len(word2)
        s = ""
        minimum = min(lew1, lew2)
        r = []

        for i in range(minimum):
            r.append(word1[i])
            r.append(word2[i])
        
        if lew1 > lew2:
            r.append(word1[minimum:])
        elif lew1 < lew2:
            r.append(word2[minimum:])
        
        return s.join(r)
