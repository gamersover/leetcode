class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        max_len = 0
        start, end = 0, 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = True
               
                elif s[i] == s[j]:
                    if j - i > 1:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = True
                        
                else:
                    dp[i][j] = False
                    
                if dp[i][j] and max_len < j - i + 1:
                    start = i
                    end = j + 1
                    max_len = j - i + 1 
        
        return s[start:end]
