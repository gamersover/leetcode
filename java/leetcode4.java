class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length < nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }

        int m = nums1.length, n = nums2.length;

        int halfLen = (m + n + 1) >> 1;
        int jleft = 0, jright = n;
        int i = 0, j = 0;
        while(jleft <= jright) {
            j = (jleft + jright) >> 1;
            i = halfLen - j;
            if (j < n && nums2[j] < nums1[i-1]) jleft = j + 1;
            else if(j > 0 && nums1[i] < nums2[j-1]) jright =  j - 1;
            else break;
        }

        double maxLeft, minRight;
        if (j == 0) maxLeft = nums1[i-1];
        else if(j == n && i==0) maxLeft = nums2[j-1];
        else maxLeft = Math.max(nums1[i-1], nums2[j-1]);

        if ((m + n) % 2 == 1) return maxLeft;

        if (j == n) minRight = nums1[i];
        else if(j == 0 && i == m) minRight = nums2[j];
        else minRight = Math.min(nums1[i], nums2[j]);
    
        return (maxLeft + minRight) / 2;
    }
}