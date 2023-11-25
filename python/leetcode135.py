from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy_arr = [1 for i in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy_arr[i] = candy_arr[i-1] + 1
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] < ratings[i-1] and candy_arr[i] >= candy_arr[i-1]:
                candy_arr[i-1] = candy_arr[i] + 1
        return sum(candy_arr)


Solution().candy([1, 3, 5, 4, 2, 1, 5])