class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m -1
        pointer2 = n -1

        for i in range(m + n - 1, -1, -1):
            if pointer1 < 0 or pointer2 < 0:
                break
            elif nums1[pointer1] > nums2[pointer2]:
                print(f'pointer1 = {pointer1}')
                nums1[i] = nums1[pointer1]
                pointer1 -= 1
            elif nums1[pointer1] <= nums2[pointer2]:
                print(f'pointer2 = {pointer2}')
                nums1[i] = nums2[pointer2]
                pointer2 -= 1

        print(f'pointer1 = {pointer1}, pointer2 = {pointer2}')
        if pointer2 >= -1:
            for i in range(pointer2 + 1):
                nums1[i] = nums2[i]