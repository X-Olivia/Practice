class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        size = len(nums1) + len(nums2)
        p1 = p2 = pos = 0

        if size%2 == 0: #even
            while pos != size//2:
                if nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1
                pos += 1
            med = ### 不对，我除了要找2还要找3（例子4个数）





        else: