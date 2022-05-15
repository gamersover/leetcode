from math import comb
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, combinations, tmp, index):
            if target < 0:
                return
            if target == 0:
                combinations.append(tmp[:])
                return
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    return
                tmp.append(candidates[i])
                dfs(candidates, target - candidates[i], combinations, tmp, i)
                tmp.pop()

        combinations = []
        tmp = []
        candidates = sorted(candidates)
        dfs(candidates, target, combinations, tmp, 0)
        return combinations
