class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque


        seen = deque()
        max_length = 0

        for char in s:
            while char in seen:
                seen.popleft()
            seen.append(char)
            max_length = max(max_length, len(seen))
        
        return max_length