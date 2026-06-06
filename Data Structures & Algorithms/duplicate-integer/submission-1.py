class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checklist = set(nums)
        if len(checklist) != len(nums):
            return True
        else:
            return False