class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].casefold() == s[right].casefold():
                left += 1
                right -= 1
            else:
                print(f's[left] = {s[left]}, s[right] = {s[right]}')
                return False

        return True 