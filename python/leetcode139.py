from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        word_set = set(wordDict)
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in word_set:
                    dp[i+1] = True
                    break
        return dp[len(s)]



s = "leetcode"
wordDict = ["leet", "code"]
print(Solution().wordBreak(s, wordDict))