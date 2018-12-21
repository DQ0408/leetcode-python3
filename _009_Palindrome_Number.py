# -*- coding: utf-8 -*-
"""
Created on 2018/12/03 16:52
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
