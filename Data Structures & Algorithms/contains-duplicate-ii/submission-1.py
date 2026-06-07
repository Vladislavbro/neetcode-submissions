class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        
        for left in range (len(nums)):
            right: int = left + 1
            while abs(left - right) <= k and right < len(nums):
                if nums[left] == nums[right]:
                    return True
                right += 1
            
        # print('чебля')    
        return False