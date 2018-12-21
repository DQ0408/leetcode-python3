# -*- coding: utf-8 -*-
"""
Created on 2018/12/02 17:12
@author: Sucre
@email: qian.dong.2018@gmail.com
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_ = 0
        start = 0
        dict_ = {}
        for i in range(len(s)):
            if s[i] in dict_ and start <= dict_[s[i]]:  # 重复
                start = dict_[s[i]] + 1
            else:  # 不重复
                max_ = max(i - start + 1, max_)
            dict_[s[i]] = i
        return max_
