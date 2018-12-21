# -*- coding: utf-8 -*-
"""
Created on 2018/12/19 10:49
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for _ in range(len(nums)):
            if nums[i]==val:
                del nums[i]
            else:
                i+=1
        return len(nums)