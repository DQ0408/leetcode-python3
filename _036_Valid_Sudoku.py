# -*- coding: utf-8 -*-
"""
Created on 2018/12/21 20:42
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(line):
            num = {}
            for n in line:
                if not n in num:
                    if n!='.':
                        num[n] = 0
                else:
                    return False
            return True
        for l in board:
            if not isValid(l):
                return False
        for i in range(9):
            line = [l[i] for l in board]
            if not isValid(line):
                return False
        for i in range(3):
            l = []
            l.append(board[i * 3])
            l.append(board[i * 3 + 1])
            l.append(board[i * 3 + 2])
            for j in range(3):
                line = []
                for k in range(3):
                    line += l[k][j * 3:j * 3 + 3]
                if not isValid(line):
                    return False
        return True
