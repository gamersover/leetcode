from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, 1
        curr_state = "desc"
        all_pairs = []
        while r < len(height):
            if (height[r] < height[r-1]) or (height[r] == height[r-1] and height[r-1] != height[l]):
                if curr_state == "desc":
                    r += 1
                else:
                    all_pairs.append((l, r-1))
                    l = r - 1
                    curr_state = "desc"
            else:
                if r - l > 1 and curr_state == "desc":
                    curr_state = "asc"
                elif r - l == 1:
                    l = r
                r += 1
        if curr_state != "desc":
            all_pairs.append((l, r-1))

        area = 0
        for pair in all_pairs:
            s = (pair[1] - pair[0] - 1) * min(height[pair[1]], height[pair[0]])
            for i in range(pair[0] + 1, pair[1]):
                s -= height[i]
            area += s
        return area


print(Solution().trap([4,2,0,3,2,5]))

