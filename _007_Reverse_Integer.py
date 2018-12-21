# -*- coding: utf-8 -*-
"""
Created on 2018/12/03 16:25
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        sign = x // abs(x)
        x = str(abs(x))[::-1]
        if -2 ** 31 <= int(x) * sign <= 2 ** 31 - 1:
            return int(x) * sign
        else:
            return 0
