class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        total_len = len(num1) + len(num2)
        arr = [0]*total_len
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                arr[i+j+1] += int(num1[i]) * int(num2[j])

        for i in range(total_len-1, 0, -1):
            arr[i-1] += arr[i] // 10
            arr[i] %= 10

        start = 1 if arr[0] == 0 else 0
        return "".join(map(str, arr[start:]))
