class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            left_number = s[left]
            right_number = s[right]
            s[left] = right_number
            s[right] = left_number
            left += 1
            right -= 1        