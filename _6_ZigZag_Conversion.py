# -*- coding: utf-8 -*-
"""
Created on 2018/12/03 15:06
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        col = self.compute_col(len(s), numRows) + 1
        new_array = [[''] * col for _ in range(numRows)]
        rs = list(range(numRows)) + (list(range(numRows))[::-1])[1:-1]
        for i in range(len(s)):
            c = self.compute_col(i, numRows)
            r = rs[i % (2 * numRows - 2)]
            new_array[r][c] = s[i]
        return ''.join([''.join(new_array[i]) for i in range(numRows)])

    def compute_col(self, length, numRows):
        length += 1
        col = length // (2 * numRows - 2) * (numRows - 1)
        if 0 < length - length // (2 * numRows - 2) * (2 * numRows - 2) <= numRows - 1:
            col += 1
        elif length - length // (2 * numRows - 2) * (2 * numRows - 2) == 0:
            pass
        else:
            col += length - length // (2 * numRows - 2) * (2 * numRows - 2) - numRows + 1
        return col - 1


if __name__ == "__main__":
    s = Solution()
    print(s.convert('PAYPALISHIRING', 1))
    print(s.convert('PAYPALISHIRING', 4))
