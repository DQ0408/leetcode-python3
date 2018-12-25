# -*- coding: utf-8 -*-
"""
Created on 2018/12/22 21:14
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def generate_seq(n):
            if n==1:
                return '1'
            last_seq = generate_seq(n-1)
            match_str = last_seq[0]
            cnt = 0
            seq = ''
            for s in last_seq:
                if s==match_str:
                    cnt+=1
                else:
                    seq += str(cnt)+match_str
                    match_str = s
                    cnt = 1
            seq+=str(cnt)+match_str
            return seq
        return generate_seq(n)

