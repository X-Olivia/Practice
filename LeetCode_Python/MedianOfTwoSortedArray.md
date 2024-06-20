## Question

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return the median of the two sorted arrays.

The overall runtime complexity should be \(O(\log(m+n))\).

### Example 1:
Input: `nums1 = [1,3]`, `nums2 = [2]`  
Output: `2.00000`  
Explanation: merged array = `[1,2,3]` and median is `2`.

### Example 2:
Input: `nums1 = [1,2]`, `nums2 = [3,4]`  
Output: `2.50000`  
Explanation: merged array = `[1,2,3,4]` and median is `(2 + 3) / 2 = 2.5`.

### Constraints:
- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Analysis:

To find the median of two sorted arrays, we can merge the arrays and then find the median of the merged array. Given that the arrays are already sorted, we can use a merge sort approach.

### Method 1: Using a New Array for Merging
This method involves creating a new array to store the merged elements and then finding the median of this new array.

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size = len(nums1) + len(nums2)
        p1 = p2 = pos = 0
        new_list = [0] * size
        
        while p1 < len(nums1) or p2 < len(nums2):
            num1 = nums1[p1] if p1 < len(nums1) else float('inf')
            num2 = nums2[p2] if p2 < len(nums2) else float('inf')
            
            if num1 < num2:
                new_list[pos] = num1
                p1 += 1
            else:
                new_list[pos] = num2
                p2 += 1
            pos += 1
        
        if size % 2 == 0:
            med = (new_list[size // 2 - 1] + new_list[size // 2]) / 2.0
        else:
            med = new_list[size // 2]
        
        return med
```

### Method 2: Using Binary Search for Optimization
Considering the required time complexity \(O(\log(m+n))\), we can optimize the solution using binary search.

```python
class Solution(object):
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
```