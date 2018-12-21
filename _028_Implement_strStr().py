# -*- coding: utf-8 -*-
"""
Created on 2018/12/19 10:51
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        l = len(needle)
        if len(haystack)==0 and l==0:
            return 0
        for i in range(len(haystack)-l + 1):
            if haystack[i:i+l]==needle:
                return i
        return -1
