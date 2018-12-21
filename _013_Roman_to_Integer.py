# -*- coding: utf-8 -*-
"""
Created on 2018/12/13 13:31
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapRtoI = {}
        mapRtoI['I'] = 1
        mapRtoI['V'] = 5
        mapRtoI['X'] = 10
        mapRtoI['L'] = 50
        mapRtoI['C'] = 100
        mapRtoI['D'] = 500
        mapRtoI['M'] = 1000
        Numbers = []
        for char in s:
            Numbers.append(mapRtoI[char])
        result = 0
        special_num = [1, 10, 100]
        mapSpecial = {1: [5, 10], 10: [50, 100], 100: [500, 1000]}

        def dp(i):  # Numbers[i:]代表的数
            global result
            if i == len(Numbers):
                return 0
            else:
                if Numbers[i] in special_num:
                    if i + 1 < len(Numbers) and Numbers[i + 1] in mapSpecial[Numbers[i]]:
                        result += (Numbers[i + 1] - Numbers[i] + dp(i + 2))
                    else:
                        result += Numbers[i] + dp(i + 1)
                else:
                    result += Numbers[i] + dp(i + 1)
        dp(0)
        return result
