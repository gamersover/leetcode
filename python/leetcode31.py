from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        desc_index = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                desc_index = i
                break

        if desc_index > 0:
            start = desc_index
            end = len(nums)
            while start < end:
                mid = (start + end) >> 1
                if nums[mid] > nums[desc_index-1]:
                    start = mid + 1
                elif nums[mid] <= nums[desc_index-1]:
                    end = mid

            find_index = start - 1
            nums[find_index], nums[desc_index-1] = nums[desc_index-1], nums[find_index]

        for i in range(0, (len(nums)-desc_index) // 2):
            nums[desc_index+i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[desc_index+i]


arr = [3, 2, 1]
Solution().nextPermutation(arr)

print(arr)


