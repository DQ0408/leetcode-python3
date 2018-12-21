# -*- coding: utf-8 -*-
"""
Created on 2018/12/14 15:16
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0]+nums[1]+nums[-1]
        min_dis = abs(target-res)
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if abs(s-target)<min_dis:
                    res = s
                    min_dis = abs(s-target)
                if s==target:
                    return target
                else:
                    if s>target:
                        k-=1
                    else:
                        j+=1
        return res