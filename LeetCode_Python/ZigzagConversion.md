## Question


The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000



## Analysis

The formats should be like: 
### 4 rows
0     6       12
1   5 7    11 13
2 4   8 10
3     9 

### 3 rows
0   4   8     12
1 3 5 7 9  11 13
2   6   10


When I saw this problem, I thought we could use a 2D array. First, initialize a 2D array, and then perform some mathematical operations on the index of each character to get its position in the 2D array and store it there. After that, traverse the 2D array to get the new string. The difficulty lies in finding the index transformation rule. However, it seems somewhat complicated, and I don't think it is the best solution. To save time, I gave up on this approach and considered other solutions.

By observing the zigzag pattern, I noticed that for cases where numRows is 1 or numRows is greater than the length of the string, the output is the same as the input. These can be treated as special cases:
```shell
if numRows == 1 or numRows >= len(s):
    return s
```
From this, we can see that the string is written in a zigzag pattern between the top and bottom rows. When a character reaches the top or bottom row, the direction changes. The exact column where the middle characters are placed is not important; we only need to know which row they belong to.

Hence, the code logic is as follows:


- Handle special cases
- Create an empty list rows of size numRows, where each element represents a row in the transformed string.
- Create variables row and dir to track the current position and direction. When encountering the top or bottom row, change the direction.

Based on this logic, the code is as follows:

## Code

```shell
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        row = 0
        dir = 1
        for i in s:
            rows[row] += i
            if row == 0:
                dir = 1
            elif row == numRows - 1:
                dir = -1
            row += dir
        return "".join(rows)
```


## Complexity:
- Time complexity : O(n), where n is the length of the string
- Space complexity: O(numRows), where numRows is the number of rows, cause we create a list of lists to store the caharacters.