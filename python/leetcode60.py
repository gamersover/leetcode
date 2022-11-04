class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fractal = [1]*n
        for i in range(1, n):
            fractal[i] = fractal[i-1] * i
        nlist = list(range(1, n+1))
        ans = ""
        for i in range(n):
            ind = (k-1) // fractal[n-i-1]
            k %= fractal[n-i-1]
            ans += str(nlist[ind])
            nlist.pop(ind)
        return ans


print(Solution().getPermutation(5, 1))