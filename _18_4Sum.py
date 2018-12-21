# -*- coding: utf-8 -*-
"""
Created on 2018/12/14 16:04
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()

        def twoSum(nums, target):
            if len(nums) == 0:
                return []
            l = 0
            r = len(nums) - 1
            result = []
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    result.append([nums[l], nums[r]])
                    while l + 1 < r and nums[l + 1] == nums[l]:
                        l += 1
                    while l < r - 1 and nums[r - 1] == nums[r]:
                        r -= 1
                    l, r = l + 1, r - 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
            return result

        def nSum(nums, target, n):
            res = []
            if n == 2:
                return twoSum(nums, target)
            else:
                for idx, num in enumerate(nums):
                    if idx > 0 and num == nums[idx - 1]:
                        continue
                    next_res = nSum(nums[idx + 1:], target - num, n - 1)
                    for ns in next_res:
                        if len(ns) == n - 1:
                            res.append([num] + ns)
            return res

        return nSum(nums, target, 4)
