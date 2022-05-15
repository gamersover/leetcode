

class Solution {
public:
    int divide(int dividend, int divisor) {
        // 当dividend和divisor为INT_MIN时，不能使用绝对值，因为会溢出
        if (dividend == 0) return 0;
        if (dividend == INT_MIN){
            if (divisor == -1) return INT_MAX;
            if (divisor == 1) return INT_MIN;
        } 
        if (divisor == INT_MIN) {
            if (dividend == INT_MIN) return 1;
            return 0;
        }

        bool isPositive = true;
        if (dividend > 0) {
            dividend = -dividend;
            isPositive = !isPositive;
        }
        if (divisor > 0) {
            divisor = -divisor;
            isPositive = !isPositive;
        }

        int result = div(dividend, divisor);
        return isPositive ? result : -result;
    }

    int div(int dividend, int divisor){
        if (dividend > divisor) return 0;
        int sum = divisor;
        int result = 1;
        // 注意： 不能使用sum - dividend，因为会先计算-dividend，从而导致溢出
        while ((dividend - sum) <= sum){
            sum += sum;
            result += result;
        }
        return result + div(dividend - sum, divisor);
    }
};


int main(){
    int re = Solution().divide(10, 3);
    return 0;
}