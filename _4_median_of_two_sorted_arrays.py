# -*- coding: utf-8 -*-
"""
Created on 2018/12/03 11:27
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        cnt1 = 0
        cnt2 = 0
        m_plus_n = len(nums1) + len(nums2)
        new_nums = []
        for i in range(m_plus_n):
            if cnt1 >= len(nums1):
                new_nums += nums2[cnt2:]
                break
            elif cnt2 >= len(nums2):
                new_nums += nums1[cnt1:]
                break
            else:
                if nums1[cnt1] > nums2[cnt2]:
                    new_nums.append(nums2[cnt2])
                    cnt2 += 1
                else:
                    new_nums.append(nums1[cnt1])
                    cnt1 += 1
        if m_plus_n % 2:
            return new_nums[m_plus_n // 2]
        else:
            return (new_nums[m_plus_n // 2 - 1] + new_nums[m_plus_n // 2]) / 2


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
