class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m < n:
            m, n, nums1, nums2 = n, m, nums2, nums1
        
        half_len = (m + n + 1) >> 1
        jleft, jright = 0, n
        while jleft <= jright:
            j = (jleft + jright) >> 1
            i = half_len - j
            if j < n and nums2[j] < nums1[i-1]:
                jleft = j + 1
            elif j > 0 and nums1[i] < nums2[j-1]:
                jright = j - 1
            else:
                break
        
        if j == 0:
            max_left = nums1[i-1]
        elif j == n and i == 0:
            max_left = nums2[j-1]
        else:
            max_left = max(nums1[i-1], nums2[j-1])
        
        if (m + n) % 2 == 1:
            return max_left
        
        if j == n:
            min_right = nums1[i]
        elif j == 0 and i == m:
            min_right = nums2[j]
        else:
            min_right = min(nums1[i], nums2[j])
        
        return (max_left + min_right) / 2
