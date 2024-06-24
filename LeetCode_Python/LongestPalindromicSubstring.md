## Question
Given a string `s`, return the longest palindromic substring in `s`.

### Example 1:
Input: `s = "babad"`
Output: `"bab"`
Explanation: `"aba"` is also a valid answer.

### Example 2:
Input: `s = "cbbd"`
Output: `"bb"`

### Constraints:
1. `1 <= s.length <= 1000`
2. `s` consists of only digits and English letters.

## Analysis
The problem is to find the longest palindromic substring in a given string. Recalling the previously written palindrome check method, you can determine if a string is a palindrome by using two pointers, one pointing to the head and one to the tail, and comparing characters while moving towards the center.

```python
while i <= j:
    if string[i] == string[j]:
        i += 1
        j -= 1
        continue
    else:
        return False
return True
```

I initially thought of a rather cumbersome method: start by taking the first character, find the same character in the rest of the string as the other end, check if it forms a symmetric string, and if so, save the length in a dictionary. If not, move to the second character and continue the check.

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        dic = {}
        i = 0
        for c in s:
            indices = self.idxs(s[i:], c)
            for idx in indices:
                substring = s[i: i + idx + 1]
                if self.isPal(substring):
                    dic[len(substring)] = substring
            i += 1
        return dic[max(dic, default=0)]

    def isPal(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    def idxs(self, string: str, char_to_find: str) -> list:
        indices = []
        for idx in range(len(string)):
            if string[idx] == char_to_find:
                indices.append(idx)
        return indices 

sol = Solution()
```

However, during the process, I found that this method is quite complex and bug-prone, even with two auxiliary functions. After modifications, many test cases still timed out, so I abandoned this method and thought of a new one. 

While studying, I discovered that the method for checking palindromes can be simplified to `string == string[::-1]`. This means if a string equals its reversed version, it is a palindrome.

Moreover, the step of finding the same characters can be removed; directly checking each character is sufficient since finding the same character is also a character-by-character search. (Recently, I haven't rested well and my brain is foggy...)

## Code-Method 1

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(substring: str) -> bool:
            return substring == substring[::-1]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                if isPalindrome(substring) and len(substring) > len(longest_palindrome):
                    longest_palindrome = substring
        
        return longest_palindrome
```

This method has low space complexity but high time complexity. However, I couldn't think of other methods. 

Therefore, I learned online:

This method uses the center expansion method to find the longest palindromic substring in a string.

## Code-Method 2

```python
# Two conditions: one is center symmetry, the other is axis symmetry
# Expand from the middle outwards
# Use dynamic programming
class Solution:
    def longestPalindrome(self, s: str) -> str:      
        palindrome = ""
        for i in range(len(s)):
            # Check for palindrome of odd length
            len1 = len(self.getlongestpalindrome(s, i, i))
            if len1 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i)

            # Check for palindrome of even length
            len2 = len(self.getlongestpalindrome(s, i, i + 1))
            if len2 > len(palindrome):
                palindrome = self.getlongestpalindrome(s, i, i + 1)
        
        return palindrome

    def getlongestpalindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1 : r]
```
I think the core of this method is: Seek rather than check.