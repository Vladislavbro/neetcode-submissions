class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        long_prefix = min(strs)
        for word in strs:
            while not word.startswith(long_prefix):
                long_prefix = long_prefix[:-1]
        return long_prefix
