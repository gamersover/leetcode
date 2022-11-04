from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            k = "".join(sorted(s))
            d[k] = d.get(k, []) + [s]
        return list(d.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))