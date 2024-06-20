
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def findKthSmallest(A, B, k):
            lenA, lenB = len(A), len(B)
            if lenA > lenB:
                return findKthSmallest(B, A, k)
            if lenA == 0:
                return B[k-1]
            if k == 1:
                return min(A[0], B[0])
            
            i = min(lenA, k // 2)
            j = min(lenB, k // 2)
            
            if A[i - 1] > B[j - 1]:
                return findKthSmallest(A, B[j:], k - j)
            else:
                return findKthSmallest(A[i:], B, k - i)
        
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            return findKthSmallest(nums1, nums2, total_len // 2 + 1)
        else:
            return (findKthSmallest(nums1, nums2, total_len // 2) + findKthSmallest(nums1, nums2, total_len // 2 + 1)) / 2.0
        
