# -*- coding: utf-8 -*-
"""
Created on 2018/12/20 14:16
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        _nums = nums[::-1]
        idx = -1
        for i in range(1, len(_nums)):
            if _nums[i] < _nums[i - 1]:
                idx = i
                break
        if idx != -1:
            tmp_nums = _nums[:idx]
            to_swap = min([n for n in tmp_nums if n > _nums[idx]])  # min(tmp_nums)
            tmp_nums[tmp_nums.index(to_swap)] = _nums[idx]
            _nums[idx] = to_swap
            _nums[:idx] = tmp_nums[::-1]
            _nums = _nums[::-1]
        for i in range(len(nums)):
            nums[i] = _nums[i]

        # def get_all_num(nums):
        #     res = []
        #     if len(nums) == 1:
        #         return [str(nums[0])]
        #     for idx, num in enumerate(nums):
        #         tmp_nums = [num for i, num in enumerate(nums) if i != idx]
        #         tmp_nums = get_all_num(tmp_nums)
        #         for n in tmp_nums:
        #             if type(n) == type("0"):
        #                 res.append([str(num)] + [n])
        #             else:
        #                 res.append([str(num)] + n)
        #     return res
        #
        # res = get_all_num(nums)
        # res = [int("".join(n)) for n in res]
        # res = list(set(res))
        # res.sort()
        # _nums = [str(n) for n in nums]
        # _nums = int("".join(_nums))
        # try:
        #     _nums = res[res.index(_nums) + 1]
        #
        # except:
        #     _nums = res[0]
        # _nums = str(_nums)
        # for i in range(len(nums)):
        #     nums[i] = int(_nums[i])
