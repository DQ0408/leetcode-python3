# -*- coding: utf-8 -*-
"""
Created on 2018/12/03 11:41
@author: Sucre
@email: qian.dong.2018@gmail.com
"""

# 参考：https://leetcode.com/problems/longest-palindromic-substring/discuss/124037/Python-using-sliding-windows
class Solution:
    def longestPalindrome(self, s):
        ans = ''
        max_len = 0
        n = len(s)
        DP = [[0] * n for _ in range(n)]
        for i in range(n):
            DP[i][i] = True
            ans = s[i]
            max_len = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                DP[i][i + 1] = True
                ans = s[i:i + 2]
                max_len = 2
        for j in range(2, n):
            for i in range(0, j - 1):
                if DP[i + 1][j - 1] and s[i] == s[j]:
                    DP[i][j] = True
                    if max_len < j - i + 1:
                        ans = s[i:j + 1]
                        max_len = j - i + 1
        return ans

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        for i in reversed(range(len(s))):
            for start in range(len(s)-i):
                xstring = s[start:start+i+1]
                if xstring == xstring[::-1]:
                    return xstring
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     length = len(s)
    #     P = [[False for _ in range(length)] for _ in range(length)]
    #     for i in range(length):
    #         P[i][i] = True
    #         if i < length - 1:
    #             if s[i] == s[i + 1]:
    #                 P[i][i + 1] = True
    #                 P[i + 1][i] = True
    #     for _ in range(length // 2):
    #         for i in range(length):
    #             for j in range(length):
    #                 try:
    #                     if P[i + 1][j - 1] and s[i] == s[j]:
    #                         P[i][j] = True
    #                 except:
    #                     pass
    #     _max = 0
    #     _i = 0
    #     _j = 0
    #     for i, p in enumerate(P):
    #         j = length - p[::-1].index(True)
    #         if j - i > _max:
    #             _max = j - i
    #             _i = i
    #             _j = j
    #     return s[_i:_j]
