class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        seen = set()
        left = 0
        
        for right in range(len(nums)):
            if abs(left - right) > k:
                seen.discard(nums[left])
                left +=1
            if nums[right] in seen:
                return True
            seen.add(nums[right])

        return False