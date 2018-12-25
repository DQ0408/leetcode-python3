# -*- coding: utf-8 -*-
"""
Created on 2018/12/23 19:51
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        for i in range(len(nums)):
            while len(nums) >= nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i
