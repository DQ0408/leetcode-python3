# -*- coding: utf-8 -*-
"""
Created on 2018/12/03 16:31
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        digits = '0123456789'
        sign = '+-'
        str = str.strip()
        try:
            result = int(str)
        except:
            s = ''
            try:
                if str[0] in sign or str[0] in digits:
                    s += str[0]
                    for char in str[1:]:
                        if char in digits:
                            s += char
                        else:
                            break
                result = int(s)
            except:
                result = 0
        if result < -2 ** 31:
            return -2**31
        elif result > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return result