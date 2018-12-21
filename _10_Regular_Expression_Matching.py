# -*- coding: utf-8 -*-
"""
Created on 2018/12/03 16:54
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution(object):
    def isMatch(self, text, pattern):
        memo = {}

        def dp(i, j):  # dp(i, j): does text[i:] and pattern[j:] match ?
            if (i, j) not in memo:
                if j != len(pattern):
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j + 1 < len(pattern) and pattern[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)
                else:
                    ans = i == len(text)
                memo[i, j] = ans
            return memo[i, j]
        return dp(0, 0)
