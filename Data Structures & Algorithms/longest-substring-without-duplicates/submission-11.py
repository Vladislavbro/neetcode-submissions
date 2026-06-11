class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0

        for left in range(len(s)):
            current_lenght = 0
            seen = set()
            for right in range(left, len(s)):
                if s[right] not in seen:
                    current_lenght += 1
                    seen.add(s[right])
                    max_length = max(current_lenght, max_length)
                else:
                    break

        return max_length
