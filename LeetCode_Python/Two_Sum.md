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


## Solution1

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
        for i in nums:
            first_index = nums.index(i)
            second = target - i
            next_index = first_index + 1
            temp_nums = nums[next_index: ]
            if second in temp_nums:
                return (first_index, temp_nums.index(second) + next_index)
        return "no solution."
```

## Solution2

### Analysis

However, this method consume too much time, so we can try to solve it by Hash map.

The first time I write in Hash map is:

```shell
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in nums:
            if target - i not in dict:
                dict[i] = nums.index(i)
            else:
                return(nums.index(target - i),nums.index(i))
        return "no solution"
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
        return "no solution"
```



