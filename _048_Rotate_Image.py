# -*- coding: utf-8 -*-
"""
Created on 2018/12/25 14:19
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            row1 = matrix[i][i:n - i]
            col1 = [m[n - i - 1] for m in matrix][i:n - i][::-1]
            row2 = matrix[-i - 1][i:n - i]
            col2 = [m[i] for m in matrix][i:n - i][::-1]
            matrix[i][i:n - i] = col2
            matrix[-i - 1][i:n - i] = col1
            for j in range(i, n - i):
                print(j)
                matrix[j][-i - 1] = row1[j - i]
                matrix[j][i] = row2[j - i]
