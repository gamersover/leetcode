from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.ans = []
        self.search(s, wordDict, 0, [])
        return self.ans

    def search(self, s, wordDict, start, res):
        if len(s) == start:
            self.ans.append(" ".join(res))
            return
        for w in wordDict:
            n = len(w)
            if start + n <= len(s) and s[start:start+n]==w:
                self.search(s, wordDict, start+n, res + [w])


if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    print(Solution().wordBreak(s, wordDict))