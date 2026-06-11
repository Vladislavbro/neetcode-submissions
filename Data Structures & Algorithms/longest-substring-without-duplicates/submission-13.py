class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import deque


        seen = deque()
        seen_set = set()
        max_length = 0

        for char in s:
            while char in seen_set:
                seen_set.discard(seen.popleft())

            seen.append(char)
            seen_set.add(char)
            max_length = max(max_length, len(seen))
        
        return max_length