# -*- coding: utf-8 -*-
"""
Created on 2018/12/20 11:31
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == "" or len(words) == 0:
            return []
        n_word = len(words[0])
        n = len(words)
        n_words = n * n_word
        word_set = set(words)
        res = set()
        for i in range(len(s) - n_words + 1):
            sub_str = s[i:i + n_words]
            tmp_words = [word for word in words]
            for j in range(n):
                word = sub_str[j * n_word:j * n_word + n_word]
                if not word in word_set:
                    break
                else:
                    try:
                        del tmp_words[tmp_words.index(word)]
                    except:
                        break
            if len(tmp_words) == 0:
                res.add(i)
        return list(res)

        # def strStr(haystack, needle):
        #     """
        #     :type haystack: str
        #     :type needle: str
        #     :rtype: int
        #     """
        #     l = len(needle)
        #     res = [-1]
        #     if len(haystack) == 0 and l == 0:
        #         return res
        #     for i in range(len(haystack) - l + 1):
        #         if haystack[i:i + l] == needle:
        #             res.append(i)
        #     return res
        #
        # def get_all_str(a):
        #     res = []
        #     if len(a) == 1:
        #         return [a[0]]
        #     for idx, s in enumerate(a):
        #         a_tmp = [st for i, st in enumerate(a) if i != idx]
        #         all_str = get_all_str(a_tmp)
        #         for ss in all_str:
        #             tmp = s + ss
        #             res.append(tmp)
        #     return res
        #
        # all_str = list(set(get_all_str(words)))
        # res = []
        # for chars in all_str:
        #     idx = strStr(s, chars)
        #     if len(idx) != 1:
        #         res += idx[1:]
        # return res
