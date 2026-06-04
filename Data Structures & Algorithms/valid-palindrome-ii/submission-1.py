class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # мы в точке где буквы не сопали
                # допустим s = "abbda". left = 1, right = 3
                return self.isPalindrome(s[left + 1:right + 1]) or self.isPalindrome(s[left:right])
            left += 1
            right -= 1
        return True