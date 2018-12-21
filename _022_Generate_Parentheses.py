# -*- coding: utf-8 -*-
"""
Created on 2018/12/18 13:25
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def generate(s, left, right):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if left < n:
                generate(s + '(', left + 1, right)
            if right < left:
                generate(s + ')', left, right + 1)

        generate('', 0, 0)
        return ans
