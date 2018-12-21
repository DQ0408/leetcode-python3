# -*- coding: utf-8 -*-
"""
Created on 2018/12/19 11:01
@author: Sucre
@email: qian.dong.2018@gmail.com
"""
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        res = int(str(dividend/divisor).split('.')[0])
        if res not in range(-2**31, 2**31-1):
            return 2**31-1
        return res
