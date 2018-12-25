# -*- coding: utf-8 -*-
"""
Created on 2018/12/23 22:03
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #  i needs to go from 0 to len(s) to create empty string
        DP = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        DP[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                if i < len(s) and p[j] == '*':
                    # return self.isMatch(s[1:],p) or self.isMatch(s,p[1:])
                    DP[i][j] = DP[i + 1][j] or DP[i][j + 1]
                elif i < len(s) and p[j] == '?':
                    # return self.isMatch(s[1:],p[1:])
                    DP[i][j] = DP[i + 1][j + 1]
                elif i < len(s) and j < len(p):
                    # return s[0] == p[0] and self.isMatch(s[1:],p[1:])
                    DP[i][j] = s[i] == p[j] and DP[i + 1][j + 1]
                else:  # not s and p
                    # return p[0] == '*' and self.isMatch(s,p[1:])
                    DP[i][j] = p[j] == '*' and DP[i][j + 1]
        return DP[0][0]