class Solution {
    public int maxArea(int[] height) {
        int m = 0;
        int i = 0;
        int j = height.length - 1;
        while(i < j){
            m = Math.max(m, Math.min(height[i], height[j]) * (j - i));
            if(height[i] < height[j]) i++;
            else j--;
        }
        return m;
    }
}