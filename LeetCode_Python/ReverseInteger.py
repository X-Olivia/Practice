class Solution:
    def reverse(self, x: int) -> int:
        is_negative = x<0
        x = abs(x)
        reversed = 0
        while(x != 0):
            reversed = reversed*10 + x % 10
            print(reversed)
            x //= 10
            if reversed > 2**31 - 1:
                return 0
        if is_negative == 1:
             reversed = -reversed
        return reversed


sol = Solution()
print(sol.reverse(-123))