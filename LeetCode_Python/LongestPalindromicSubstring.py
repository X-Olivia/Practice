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



sol = Solution()
print(sol.longestPalindrome("bb"))
print(sol.longestPalindrome("babad"))

