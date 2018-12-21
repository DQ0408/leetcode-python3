# -*- coding: utf-8 -*-
"""
Created on 2018/12/21 9:34
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        maxLen = 0
        for i,par in enumerate(s):
            if par=='(':
                stack.append(i)
            else:
                try:
                    stack.pop()
                    maxLen = max(maxLen, i-stack[-1])
                except:
                    stack.append(i)
        return maxLen
        # brute force
        # def isValid(s):
        #     rpar = 0
        #     for par in s:
        #         if par == '(':
        #             rpar += 1
        #         elif rpar > 0:
        #             rpar -= 1
        #         else:
        #             return False
        #     return rpar==0
        # maxLen = 0
        # for i in range(len(s)):
        #     for j in range(i+2, len(s)+1, 2):
        #         if isValid(s[i:j]):
        #             maxLen = max(maxLen, j-i)
        # return maxLen
