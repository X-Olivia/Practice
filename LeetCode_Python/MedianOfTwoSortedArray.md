## Question

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).


Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106


## Analysis：

就是把两个排列好的数组，进行排列，然后找中位数
既然已经排列好了，用快速排列就可以了
第一种方式是用一个新的数组来排列，然后找中位数
第二种方式是直接排序到中位数，不用新的数组

第二种看起来节约内存一点，首先尝试第二种

