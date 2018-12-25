# -*- coding: utf-8 -*-
"""
Created on 2018/12/22 21:25
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(running, running_sum, ind):
            for i in range(ind, len(candidates)):
                next_sum = running_sum+candidates[i]
                if next_sum<target:
                    dfs(running+[candidates[i]], next_sum, i)
                elif next_sum==target:
                    res.append(running+[candidates[i]])
        dfs([],0,0)
        return res
        # def dfs(candidates, target):
        #     res = []
        #     if target == 0:
        #         return [[]]
        #     for n in candidates:
        #         if target - n >= 0:
        #             nx_res = dfs(candidates, target - n)
        #             for r in nx_res:
        #                 res.append([n] + r)
        #     return res
        #
        # res = dfs(candidates, target)
        # for i, r in enumerate(res):
        #     res[i].sort()
        #     res[i] = str(res[i])
        # res = list(set(res))
        # for i, r in enumerate(res):
        #     res[i] = eval(res[i])
        # return res
