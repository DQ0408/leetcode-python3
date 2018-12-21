# -*- coding: utf-8 -*-
"""
Created on 2018/12/21 13:33
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        def find_pivot(nums,l,r):
            if nums[l]<nums[r]:
                return 0
            if l+1==r:
                return r
            mid = (l+r)//2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
            return find_pivot(nums, l, r)
        idx = find_pivot(nums, 0, len(nums)-1)
        def find_target(nums,target,l,r):
            if target==nums[l]:
                return l
            if target==nums[r]:
                return r
            if l==r or l+1==r:
                return -1
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid
            else:
                r = mid
            return find_target(nums, target, l, r)
        if target<nums[0]:
            return find_target(nums, target, idx, len(nums)-1)
            #在nums[idx:]里边找
        else:
            if idx==0:
                idx = len(nums)
            return find_target(nums, target, 0, idx-1)
            #在nums[:idx]里边找

# class Solution:
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         try:
#             return nums.index(target)
#         except:
#             return -1