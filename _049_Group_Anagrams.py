# -*- coding: utf-8 -*-
"""
Created on 2018/12/25 15:11
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for st in strs:
            s = list(st)
            s.sort()
            s = ''.join(s)
            if not s in res:
                res[s] = []
            res[s].append(st)
        return list(res.values())

        # def generate_dic(s):
        #     res = set()
        #     if not s:
        #         return {''}
        #     for i, char in enumerate(s):
        #         next_s = generate_dic(s[:i] + s[i + 1:])
        #         for ns in next_s:
        #             res.add(char + ns)
        #     return res
        # res = []
        # tmp = [s for s in strs]
        # for s in strs:
        #     if tmp:
        #         r = generate_dic(s)
        #         t = [tp for tp in tmp if tp in r]
        #         for tp in t:
        #             tmp.remove(tp)
        #         if t:
        #             res.append(t)
        # return res
