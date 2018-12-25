# -*- coding: utf-8 -*-
"""
Created on 2018/12/21 22:42
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def dfs(empty, rownum, colnum, sqnum, board):
            if len(empty) == 0:
                return True
            max_possible = 9
            for r, c in empty:
                p = rownum[r] & colnum[c] & sqnum[r // 3][c // 3]
                if len(p) < max_possible:
                    max_possible = len(p)
                    i, j = r, c
            if max_possible == 0:
                return False
            p = rownum[i] & colnum[j] & sqnum[i // 3][j // 3]
            empty.remove((i, j))
            for num in p:
                rownum[i].remove(num)
                colnum[j].remove(num)
                sqnum[i // 3][j // 3].remove(num)
                board[i][j] = str(num)
                if dfs(empty, rownum, colnum, sqnum, board):
                    return True
                board[i][j] = '.'
                rownum[i].add(num)
                colnum[j].add(num)
                sqnum[i // 3][j // 3].add(num)
            empty.add((i, j))
            return False
        rownum = [set(range(1,10)) for _ in range(9)]
        colnum = [set(range(1,10)) for _ in range(9)]
        sqnum = [[set(range(1,10)) for _ in range(3)] for _ in range(3)]
        empty = set()
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    rownum[i].remove(int(board[i][j]))
                    colnum[j].remove(int(board[i][j]))
                    sqnum[i//3][j//3].remove(int(board[i][j]))
                else:
                    empty.add((i,j))
        dfs(empty,rownum,colnum,sqnum,board)

    # def DFS(self, empty, colnum, rownum, sqnum, board):
    #     if len(empty) == 0:
    #         return True
    #
    #     maxpossiblelen = 9
    #     for (r, c) in empty:
    #         possible = rownum[r] & colnum[c] & sqnum[r // 3][c // 3]
    #         if len(possible) <= maxpossiblelen:
    #             maxpossiblelen = len(possible)
    #             i, j = r, c
    #
    #     if maxpossiblelen == 0:
    #         return False
    #
    #     empty.remove((i, j))
    #     possible = rownum[i] & colnum[j] & sqnum[i // 3][j // 3]
    #
    #     for num in possible:
    #         rownum[i].remove(num)
    #         colnum[j].remove(num)
    #         sqnum[i // 3][j // 3].remove(num)
    #         board[i][j] = str(num)
    #         if self.DFS(empty, colnum, rownum, sqnum, board):
    #             return True
    #         board[i][j] = '.'
    #         rownum[i].add(num)
    #         colnum[j].add(num)
    #         sqnum[i // 3][j // 3].add(num)
    #
    #     empty.add((i, j))
    #     return False
    #
    # def solveSudoku(self, board):
    #     """
    #     :type board: List[List[str]]
    #     :rtype: void Do not return anything, modify board in-place instead.
    #     """
    #
    #     colnum = []
    #     rownum = []
    #     sqnum = [[0] * 3 for _ in range(3)]
    #     for i in range(9):
    #         colnum.append(set(tuple(range(1, 10))))
    #         rownum.append(set(tuple(range(1, 10))))
    #
    #     for i in range(3):
    #         for j in range(3):
    #             sqnum[i][j] = set(tuple(range(1, 10)))
    #
    #     empty = set()
    #     for i in range(9):
    #         for j in range(9):
    #             if board[i][j] != '.':
    #                 if int(board[i][j]) in rownum[i]:
    #                     rownum[i].remove(int(board[i][j]))
    #                 if int(board[i][j]) in colnum[j]:
    #                     colnum[j].remove(int(board[i][j]))
    #                 if int(board[i][j]) in sqnum[i // 3][j // 3]:
    #                     sqnum[i // 3][j // 3].remove(int(board[i][j]))
    #             else:
    #                 empty.add((i, j))
    #
    #     self.DFS(empty, colnum, rownum, sqnum, board)
