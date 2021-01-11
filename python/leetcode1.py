class Solution:
    def twoSum(self, nums, target):
        item_idx_map = {}
        for i in range(len(nums)):
            # 获取另一个数的下标，如果不存在返回None
            j = item_idx_map.get(target - nums[i], None)
            if j is not None:
                return [i, j]
            else:
                item_idx_map[nums[i]] = i
        return []