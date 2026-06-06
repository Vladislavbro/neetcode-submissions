class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checklist = []
        for number in nums:
            if number not in checklist:
                checklist.append(number)
            else:
                return True
        return False