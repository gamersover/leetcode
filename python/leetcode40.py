from math import comb
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, combinations, temp, index):
            if target == 0:
                combinations.append(temp[:])
                return
            if target < 0 or index >= len(candidates):
                return
            i = index
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if target - candidates[i] < 0:
                    return
                temp.append(candidates[i])
                dfs(candidates, target - candidates[i], combinations, temp, i+1)
                temp.pop()

        combinations, temp = [], []
        candidates.sort()
        dfs(candidates, target, combinations, temp, 0)
        return combinations
