# -*- coding: utf-8 -*-
"""
Created on 2018/12/18 13:20
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        while l1!=None:
            l1_list.append(l1.val)
            l1 = l1.next
        l2_list = []
        while l2 != None:
            l2_list.append(l2.val)
            l2 = l2.next
        res_list = l1_list+l2_list
        if len(res_list)==0:
            return None
        res_list.sort()
        head = ListNode(res_list[0])
        cur = head
        for val in res_list[1:]:
            cur.next = ListNode(val)
            cur = cur.next
        return head


