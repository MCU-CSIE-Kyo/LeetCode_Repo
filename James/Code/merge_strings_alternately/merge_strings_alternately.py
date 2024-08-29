class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length_word1 = len(word1)
        length_word2 = len(word2)
        minimum = min(length_word1, length_word2)
        s = ""
        r = []

        for i in range(minimum):
            r.append(word1[i])
            r.append(word2[i])
        if length_word1 > length_word2:
            r.append(word1[minimum:])
        elif length_word1 < length_word2:
            r.append(word2[minimum:])
        return s.join(r)
