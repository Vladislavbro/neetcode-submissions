class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            number2 = target - number
            if number2 in seen:
                return [seen[number2], i]
            seen[number] = i