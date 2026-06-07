from collections import deque


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        seen = deque()
        left = 0
        
        for right in range(len(nums)):
            print(1)
            if abs(left - right) > k:
                print(2)
                seen.popleft()
                left +=1
            if nums[right] in seen:
                print(3)
                return True
            seen.append(nums[right])

        # print('чебля')    
        return False