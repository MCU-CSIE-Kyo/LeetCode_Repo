class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        if len(word1) == len(word2):
            for index in range(len(word1)):
               ans += word1[index] + word2[index]
        elif len(word1) > len(word2):
            for index in range(len(word2)):
                ans += word1[index] + word2[index]
            ans += word1[len(word2):]
        else:
            for index in range(len(word1)):
                ans += word1[index] + word2[index]
            ans += word2[len(word1):]
        return ans