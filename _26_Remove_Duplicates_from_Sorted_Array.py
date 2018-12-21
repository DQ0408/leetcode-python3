# -*- coding: utf-8 -*-
"""
Created on 2018/12/19 10:33
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for _ in range(len(nums)):
            if i and nums[i]==nums[i-1]:
                del nums[i]
            else:
                i+=1
        return len(nums)