from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 所有数二进制表示，如果都是3次则，某位上1的个数一定是3的倍数，由于有一个数只出现一次
        # 从而某位上1的个数 mod 3就是结果的该位上的二进制表达
        # 00 01 10 表示该位上1的个数 mod 3的结果，那么每来一个数，转移下状态，如
        # 起始状态00，来的数位上是1，则后状态为 01
        # 起始状态10，来的数位上是1，则后状态为 00， 满3个了，重新为0
        # 从而可以构建一个真值表
        a, b = 0, 0
        for x in nums:
            b = ~a & (b ^ x)
            a = ~b & (a ^ x)
        return b


print(Solution().singleNumber([3, 3, 2, 3]))