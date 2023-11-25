from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        dp = [[True for _ in range(len(s))] for _ in range(len(s))]
        # for i in range(len(s)):
        #     for j in range(i, -1, -1):
        #         dp[j][i] = (s[i] == s[j]) and (i - j < 2 or dp[j+1][i-1])
        for i in range(1, len(s)):
            for j in range(i+1):
                dp[j][i] = (s[i] == s[j]) and ((i - j <= 2) or dp[j+1][i-1])

        def split(s, start):
            if start == len(s):
                return [[]]
            ans = []
            for i in range(start, len(s)):
                if dp[start][i]:
                    pre = [s[start:i+1]]
                    for sub in split(s, i+1):
                        ans.append(pre + sub)
            return ans

        return split(s, 0)


print(Solution().partition("aabbaa"))
