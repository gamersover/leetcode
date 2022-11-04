class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if (len(s1) + len(s2)) != len(s3):
            return False

        dp = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dp[0][0] = True
        for i in range(0, len(s1)+1):
            for j in range(0, len(s2)+1):
                if i > 0:
                    dp[i][j] = (s1[i-1] == s3[i+j-1]) and dp[i-1][j]
                if j > 0:
                    dp[i][j] |= (s2[j-1] == s3[i+j-1] and dp[i][j-1])
        return dp[len(s1)][len(s2)]