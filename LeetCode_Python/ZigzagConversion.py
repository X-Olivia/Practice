class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        else:
            row = 0
            dir = 0
            rows = [""] * numRows

            for i in s:
                rows[row] += i
                if row == 0:
                    dir = 1
                elif row == numRows - 1:
                    dir = -1
                row += dir
            return "".join(rows)
            


