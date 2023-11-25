class Solution:
    def minCut(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        min_cut = [-1 for i in range(len(s)+1)]

        for i in range(len(s)):
            min_cut[i+1] = len(s)
            for j in range(i, -1, -1):
                if s[j] == s[i] and (i - j < 2 or dp[j+1][i-1]):
                    dp[j][i] = True
                    min_cut[i+1] = min(min_cut[i+1], min_cut[j] + 1)
        return min_cut[len(s)]


        # dp = [[True for i in range(len(s))] for i in range(len(s))]
        # for i in range(len(s)-2, -1, -1):
        #     for j in range(i+1, len(s)):
        #         dp[i][j] = dp[i+1][j-1] and s[i] == s[j]

        # min_cut = [-1 for i in range(len(s)+1)]
        # for i in range(len(s)):
        #     curr = len(s)
        #     for j in range(i+1):
        #         if dp[j][i]:
        #             curr = min(curr, min_cut[j]+1)
        #     min_cut[i+1] = curr
        # return min_cut[len(s)]


print(Solution().minCut("cabababcbc"))