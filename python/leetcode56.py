from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals
    

print(Solution().merge([[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]))
