# -*- coding: utf-8 -*-
"""
Created on 2018/12/14 15:38
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s="abcdefghijklmnopqrstuvwxyz"
        dtos = {}
        if digits=="":
            return []
        for i in range(5):
            dtos[i + 2] = s[i * 3:i * 3 + 3]
        dtos[7] = 'pqrs'
        dtos[8] = 'tuv'
        dtos[9] = 'wxyz'
        res = []
        for d in digits:
            res.append(dtos[int(d)])
        def dp(i):#res[i:]的组合
            result = []
            if i == len(res):
                return ['']
            chars = res[i]
            for c in chars:
                chars_next = dp(i+1)
                for cn in chars_next:
                    result.append(c+cn)
            return result
        return dp(0)


