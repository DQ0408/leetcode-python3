# -*- coding: utf-8 -*-
"""
Created on 2018/12/19 9:56
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        vals = []
        # cnt = len(lists)
        for l in lists:
            while l!=None:
                vals.append(l.val)
                l=l.next
        vals.sort()

        # while True:
        #     _min = 9999999
        #     _i = -1
        #     for i in range(cnt):
        #         l = lists[i]
        #         if l == None:
        #             continue
        #         if _min > l.val:
        #             _i = i
        #             _min = l.val
        #     if _i == -1:
        #         break
        #     vals.append(lists[_i].val)
        #     lists[_i] = lists[_i].next
        if len(vals)==0:
            return None
        head = ListNode(vals[0])
        cur = head
        for val in vals[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head
