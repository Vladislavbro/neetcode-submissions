class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            new_digit = nums[right]
            if new_digit != val:
                nums[left] = new_digit
                left += 1
        return left 