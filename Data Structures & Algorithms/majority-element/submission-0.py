class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter


        counter = Counter(nums)
        answer = counter.most_common()[0][0]
        return answer

        