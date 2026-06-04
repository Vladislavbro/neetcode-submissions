class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        min_word = min((word1, word2), key=len)
        
        for i in range(len(min_word)):
            result += word1[i]
            result += word2[i]
        
        if len(word1) != len(word2):
            max_word = max((word1, word2), key=len)
            result += max_word[len(min_word):]
        
        return result

        