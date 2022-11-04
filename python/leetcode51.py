from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        self.dfs([], n, ans)
        return ans

    def dfs(self, all_cols, n, ans):
        for c in self.find_candidates(all_cols, n):
            all_cols.append(c)
            if len(all_cols) == n:
                ans.append(self.format_ans(all_cols))

            self.dfs(all_cols, n, ans)
            all_cols.pop()

    def find_candidates(self, all_cols, n):
        all_valid = []
        for i in range(n):
            if self.isvalid(all_cols, i):
                all_valid.append(i)
        return all_valid

    def isvalid(self, all_cols, col):
        row = len(all_cols)
        for r, c in enumerate(all_cols):
            if c == col or abs(row - r) == abs(col - c):
                return False
        return True

    def format_ans(self, ans):
        s = ['.'*i + 'Q' + '.'*(len(ans)-i-1) for i in ans]
        return s


print(Solution().solveNQueens(4))
