class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        for i in range(len(s)):
            if len(stack) > 1 and s[stack[-1]] == "(" and s[i] == ")":
                stack.pop()
            else:
                stack.append(i)
        stack.append(len(s))
        print(stack)
        max_len = 0
        for i in range(1, len(stack)):
            curr_len = stack[i] - stack[i-1] - 1
            max_len = max(max_len, curr_len)
        return max_len



print(Solution().longestValidParentheses(")()())"))
