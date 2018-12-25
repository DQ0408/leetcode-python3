# -*- coding: utf-8 -*-
"""
Created on 2018/12/22 23:00
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        def dfs(running, running_sum, idx):
            if idx==len(candidates):
                return
            flag = False
            for i in range(idx, len(candidates)):
                if flag:
                    if i+1<len(candidates) and candidates[i + 1] == candidates[i]:
                        flag = True
                    else:
                        flag = False
                    continue
                n_sum = candidates[i]+running_sum
                if n_sum<target:
                    dfs(running+[candidates[i]], n_sum, i+1)
                elif n_sum==target:
                    res.append(running+[candidates[i]])
                if i+1<len(candidates) and candidates[i+1]==candidates[i]:
                    flag = True
        dfs([], 0, 0)
        return res

