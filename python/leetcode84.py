from typing import List


# 1. 单调栈分为单调递增栈和单调递减栈
# 11. 单调递增栈即栈内元素保持单调递增的栈
# 12. 同理单调递减栈即栈内元素保持单调递减的栈

# 2. 操作规则（下面都以单调递增栈为例）
# 21. 如果新的元素比栈顶元素大，就入栈
# 22. 如果新的元素较小，那就一直把栈内元素弹出来，直到栈顶比新元素小

#3.  加入这样一个规则之后，会有什么效果
# 31. 栈内的元素是递增的
# 32. 当元素出栈时，说明这个新元素是出栈元素向后找第一个比其小的元素
# 33. 当元素出栈后，说明新栈顶元素是出栈元素向前找第一个比其小的元素



class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights.append(-1)
        max_ = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                j = stack.pop()
                if len(stack) == 0:
                    w = i
                else:
                    w = i - stack[-1] - 1
                max_ = max(max_, w * heights[j])

            stack.append(i)
        return max_



arr = [2, 1, 5, 6, 2, 3]
print(Solution().largestRectangleArea(arr))

