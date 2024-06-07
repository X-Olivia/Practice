## Question

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.<br />

You may assume that each input would have exactly one solution, and you may not use the same element twice.<br />

You can return the answer in any order.<br />

## Example 1:

Input: nums = [2,7,11,15], target = 9<br />
Output: [0,1]<br />
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].<br />
Example 2:<br />

Input: nums = [3,2,4], target = 6<br />
Output: [1,2]<br />
Example 3:<br />

Input: nums = [3,3], target = 6<br />
Output: [0,1]<br />
 
## Constraints:<br />

2 <= nums.length <= 104<br />
-109 <= nums[i] <= 109<br />
-109 <= target <= 109<br />
Only one valid answer exists.<br />

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?<br />


## Method 1: Both Brute force

### Analysis：

Find two numbers which sum is the target, given an array and target number. And the same element can't be used twice.
Hence the simple solution (thinking easily) is iterating the array and create a temp array which start from i+1 to avoid useing same element. 

### Code

```shell
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            first_index = nums.index(num)
            complement = target - num
            next_index = first_index + 1
            temp_nums = nums[next_index: ]
            if complement in temp_nums:
                return (first_index, temp_nums.index(complement) + next_index)
        return []
```

## Method 1.2: Two loops

### Analysis

Also, we can run two nested loops to check every possible pair of numbers

### Code

```shell
class Solution:
    def twoSum(self, nums, target)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []
```

## Method 2: Hash Map

### Analysis

However, above methods's time/space complexity are not good enough, so we can try to solve this problem by Hash Map.

The first time I write in Hash map is:

```shell
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for num in nums:
            if target - num not in dict:
                dict[num] = nums.index(num)
            else:
                return(nums.index(target - num),nums.index(num))
        return []
```

There's a problem that if the nums in array are same, the index returned would be same, hence we need to change the way of for loop

### Code

```shell
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return(dict[target - nums[i]], i)
        return []
```



