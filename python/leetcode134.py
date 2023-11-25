from typing import List

class Solution:
    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        start, end, total_gas, total_cost = 0, 0, 0, 0
        n = len(gas)
        while start < n:
            total_gas += gas[end % n]
            total_cost += cost[end % n]
            end += 1
            if total_gas < total_cost:
                start = end
                total_gas, total_cost = 0, 0

            elif end - start >= n:
                return start
        return -1

    def canCompleteCircuit(self, gas, cost):
        # 已知 0 到 start 不满足，那么满足条件的起点只能在start后面，如果从start+1 到 len(gas)剩余油量
        # 大于0，那么起点必然是start+1，为什么呢？假设不是start+1，而是后面某个点start+i，那么即然start+i都可以走完整个路,
        # 显然start+1开始更加可以，从而有多个解，但是题目已经确定有唯一解，从而不可能是start+i
        start, total, curr = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            curr += gas[i] - cost[i]
            if curr < 0:
                start = i + 1
                curr = 0

        return -1 if total < 0 else start





