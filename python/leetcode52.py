class Solution:
    def totalNQueens(self, n: int) -> int:
        self.ans = 0
        self.dfs([], n)
        return self.ans

    def dfs(self, all_cols, n):
        for c in self.find_candidates(all_cols, n):
            all_cols.append(c)
            if len(all_cols) == n:
                self.ans += 1

            self.dfs(all_cols, n)
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


print(Solution().totalNQueens(8))