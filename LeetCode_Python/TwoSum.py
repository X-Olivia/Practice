nums = [1,3,5,4]
target = 7

class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return(dict[target - nums[i]], i)
        return "no solution"
            
            
solution = Solution()
result = solution.twoSum(nums, target)
print(result)