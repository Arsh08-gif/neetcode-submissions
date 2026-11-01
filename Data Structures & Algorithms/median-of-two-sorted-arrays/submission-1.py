class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        half = (m + n + 1) // 2

        A,B = nums1, nums2
        if m < n: 
            A,B = B,A
        
        s,e = 0,len(A)
        while (s <= e):
            mid_a = (s+e) // 2
            mid_b = half - mid_a
            l1,l2 = float("-inf"), float("-inf")
            r1,r2 = float("inf"), float("inf")
            if mid_a < len(A) : r1 = A[mid_a]
            if mid_b < len(B) : r2 = B[mid_b]
            if mid_a - 1 >= 0 : l1 = A[mid_a - 1]
            if mid_b - 1 >= 0  : l2 = B[mid_b - 1]
            if l1 > r2 : e = mid_a - 1
            elif l2 > r1 : s = mid_a + 1
            else : 
                if (m+n) % 2 == 0:
                   return (max(l1,l2) + min(r1,r2)) / 2
                else : 
                    return max(l1,l2) 


        return 0.0



# [1,2,4,6,10,13,15,19] [4,5,6,7,10,13,14,20]