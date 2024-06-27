## Question

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 
Example 1:<br>
Input: x = 123<br>
Output: 321<br>

Example 2:<br>
Input: x = -123<br>
Output: -321<br>

Example 3:<br>
Input: x = 120<br>
Output: 21<br>
 

Constraints:<br>

-2^31 <= x <= 2^31 - 1


## Analysis

we can use dic to store each digit and its corresponding index, then reverse according to the corresponding index

The approach is as follow:

1. initialize variables: dictionary, 'i', and 'reverse'
2. use whilr loop to get each digit, stopping when the highest digit is obtained
3. use for loop to generate the reversed number
4. use an if statement to check if the reversed number exceeds the range. 

## Code
```shell
class Solution:
    def reverse(self, x: int) -> int:
        dic = {}
        i = 0
        reversed = 0
        while(x/10 != 0):
            if x > 0:
                dic[i] = int(x % 10)
            else:
                dic[i] = -int(-x % 10)
            x = int(x/10)
            i+=1
        dic[i] = x
        for j in range(i):
            reversed = reversed*10 + dic[j]
        if reversed > 2147483648 or reversed < -2147483648:
            return 0      
        return reversed
```
Obviously, we can 
显然，可以去掉字典并优化细节
```shell
class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x<0
        x = abs(x)
        reversed = 0
        while(x != 0):
            reversed = reversed*10 + x % 10
            x //= 10
            if reversed > 2**31 - 1:
                return 0
        if is_negative == 1:
            reversed = -reversed
        return reversed
```


## Complexity
- Time complexity : O(n), where n is the size of the integer
- Space complexity: O(1), we don't use any additional space, rather than fixed variable is_negative and reversed
