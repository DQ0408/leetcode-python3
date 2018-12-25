# -*- coding: utf-8 -*-
"""
Created on 2018/12/25 11:44
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def __init__(self):
        self.mem = {}

    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n in [0, 1]:
            return 0
        if set(nums) == {1}:
            return n - 1

        def dfs(nums):
            if not nums:
                return 0
            if tuple(nums) in self.mem:
                return self.mem[tuple(nums)]
            min_ = 99999999
            n = nums[0]
            if n >= len(nums) - 1:
                self.mem[tuple(nums)] = 1
                return 1
            for i in range(n - 1, -1, -1):
                step = i + 1
                if step < len(nums) - 1:
                    if step + nums[step] == len(nums) - 1:
                        return 2
                    min_ = min(min_, 1 + dfs(nums[step:]))
                else:
                    min_ = min(min_, 1)
                    break
            self.mem[tuple(nums)] = min_
            return min_

        nums.insert(0, 1)
        return dfs(nums) - 1
