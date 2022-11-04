from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        pre_code = self.grayCode(n-1)
        new_code = pre_code[:]
        for p in pre_code[::-1]:
            new_code.append(p + (1 << (n-1)))
        return new_code

    def grayCode2(self, n):
        res = []
        for i in range(1 << n):
            res.append(i ^ (i >> 1))
        return res




print(Solution().grayCode2(3))
