# -*- coding: utf-8 -*-
"""
Created on 2018/12/18 12:10
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def isValid(self,s):
        """
        :type s: str
        :rtype: bool
        """
        res = True
        if len(s) % 2:
            return False
        if len(s) == 0:
            return res
        s_list = list(s)
        r_list = {')': '(', '}': '{', ']': '['}
        rflag = False
        flag = False
        for idx, char in enumerate(s_list):
            rflag = False
            if char in r_list:
                rflag = True
                cand = s_list[:idx][::-1]
                flag = False
                for l_idx, l_char in enumerate(cand):
                    if l_char == r_list[char]:
                        flag = True
                        l_idx = len(cand) - l_idx - 1
                        res = self.isValid(''.join(s_list[l_idx + 1:idx])) and res
                        break
                if flag and res:
                    s_list[l_idx] = ''
                    s_list[idx] = ''
        res = res and flag and rflag
        return res

