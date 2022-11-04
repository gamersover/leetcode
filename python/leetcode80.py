from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt, i = 1, 1
        pos_shifted = []
        while i < len(nums):
            if nums[i] != nums[i-1]:
                if cnt > 2:
                    pos_shifted.append((i, cnt - 2))
                cnt = 1
            else:
                cnt += 1
            i += 1

        if cnt > 2:
            pos_shifted.append((i, cnt - 2))

        pos_shifted.append((len(nums), 0))
        shifted = 0
        for i in range(len(pos_shifted)):
            shifted += pos_shifted[i][1]
            if i+1 < len(pos_shifted):
                for k in range(pos_shifted[i][0], pos_shifted[i+1][0]):
                    nums[k - shifted] = nums[k]
        return len(nums) - shifted


    def removeDuplicates2(self, nums):
        if len(nums) < 3:
            return len(nums)
        slow, fast = 2, 2
        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow-2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


print(Solution().removeDuplicates2([0, 0, 0, 1, 2, 2, 2]))

