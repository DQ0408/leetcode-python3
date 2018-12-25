# -*- coding: utf-8 -*-
"""
Created on 2018/12/23 20:16
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        rain = 0
        while True:
            peak1 = 0
            temp_rain = 0
            while peak1 < len(height) and height[peak1] == 0:
                peak1 += 1
            while peak1 + 1 < len(height):
                i = peak1
                while i + 1 < len(height) and height[i] > height[i + 1]:
                    i += 1
                while i + 1 < len(height) and height[i] <= height[i + 1]:
                    i += 1
                peak2 = i
                # container = height[peak1:peak2 + 1]
                if len(height[peak1:peak2 + 1]) > 2:
                    h = min(height[peak1], height[peak2])
                    for i in range(peak1, peak2+1):
                        if (h - height[i]) < 0:
                            continue
                        temp_rain += h - height[i]
                        height[i] = h
                peak1 = peak2
            if temp_rain:
                rain+=temp_rain
            else:
                break
        return rain

