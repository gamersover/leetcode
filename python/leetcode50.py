class Solution:
    def myPow1(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        m = self.myPow(x, n // 2)
        if n % 2 == 0:
            return m * m
        else:
            return x * m * m

    def myPow2(self, x: float, n: int) -> float:
        ans = 1
        while n > 0:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans

    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.myPow2(x, n)
        else:
            return 1 / self.myPow2(x, -n)


print(Solution().myPow(2.0000, -2))