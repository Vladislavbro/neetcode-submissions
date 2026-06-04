class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0

        for right in range(len(nums)):
            current = nums[right]
            if current != val:
                nums[left] = current
                left += 1
                
        return left 