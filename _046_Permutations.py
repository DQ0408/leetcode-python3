# -*- coding: utf-8 -*-
"""
Created on 2018/12/25 14:06
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        def dfs(nums):
            res = []
            if not nums:
                return [[]]
            for i,n in enumerate(nums):
                tmp = [t for idx,t in enumerate(nums) if idx!=i]
                nx_res = dfs(tmp)
                for nr in nx_res:
                    res.append([n]+nr)
            return res
        return dfs(nums)

