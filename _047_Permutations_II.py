# -*- coding: utf-8 -*-
"""
Created on 2018/12/25 14:13
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        if not nums:
            return
        def dfs(nums):
            res = []
            if not nums:
                return [[]]
            flag = False
            for i,n in enumerate(nums):
                if flag:
                    if i + 1 < len(nums) and nums[i + 1] == nums[i]:
                        flag = True
                    else:
                        flag = False
                    continue
                tmp = [t for idx,t in enumerate(nums) if idx!=i]
                nx_res = dfs(tmp)
                for nr in nx_res:
                    res.append([n]+nr)
                if i+1<len(nums) and nums[i+1]==nums[i]:
                    flag=True
            return res
        return dfs(nums)
