# -*- coding: utf-8 -*-
"""
Created on 2018/12/21 18:21
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


# -*- coding: utf-8 -*-
"""
Created on 2018/12/21 18:21
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [-1,-1]
        def binary_search(nums, target, l, r):
            if target==nums[l]:
                return l
            elif r<len(nums) and target==nums[r]:
                return r
            else:
                if l==r or l+1==r:
                    return -1
                mid = (l+r)//2
                if target > nums[mid]:
                    l = mid
                else:
                    r = mid
                return binary_search(nums,target,l,r)
        idx = binary_search(nums, target, 0, len(nums)-1)
        r = idx
        l = idx
        for n in nums[:idx][::-1]:
            if n==target:
                l-=1
            else:
                break
        for n in nums[idx+1:]:
            if n==target:
                r+=1
            else:
                break
        return [l, r]



