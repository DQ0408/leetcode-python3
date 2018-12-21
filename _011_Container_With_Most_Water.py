# -*- coding: utf-8 -*-
"""
Created on 2018/12/13 14:54
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        r = len(height) - 1
        l = 0
        max_area = 0
        while l < r:
            width = r - l
            h = min(height[r], height[l])
            max_area = max(max_area, width*h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
