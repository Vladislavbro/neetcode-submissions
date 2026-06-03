class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        dictionary = defaultdict(list)
        for word in strs:
            dictionary[tuple(sorted(word))].append(word)

        result = []
        for words in dictionary.values():
            result.append(words)

        return result