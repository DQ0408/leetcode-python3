# -*- coding: utf-8 -*-
"""
Created on 2018/12/14 13:30
@author: Sucre
@email: qian.dong.2018@gmail.com
"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[astr]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        common_prefix = strs[0]
        for i in range(len(strs)):
            common_prefix = self.get_common_prefix(common_prefix, strs[i])
        return common_prefix
    def get_common_prefix(self, a, b):
        min_len = min(len(a), len(b))
        for i in range(min_len):
            if a[i] != b[i]:
                return a[:i]
        return a[:min_len]