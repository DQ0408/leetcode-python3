# -*- coding: utf-8 -*-
"""
Created on 2018/12/21 18:37
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(nums, target, l, r):
            if target == nums[l]:
                return l
            elif r < len(nums) and target == nums[r]:
                return r
            else:
                if l == r:
                    if target > nums[r]:
                        return r + 1
                    else:
                        return r
                if l + 1 == r:
                    if target > nums[l]:
                        if target > nums[r]:
                            return r+1
                        else:
                            return r
                    else:
                        return l
                mid = (l + r) // 2
                if target > nums[mid]:
                    l = mid
                else:
                    r = mid
                return binary_search(nums, target, l, r)
        return binary_search(nums, target, 0, len(nums)-1)
