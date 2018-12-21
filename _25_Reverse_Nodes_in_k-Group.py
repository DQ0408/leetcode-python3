# -*- coding: utf-8 -*-
"""
Created on 2018/12/19 10:29
@author: Sucre
@email: qian.dong.2018@gmail.com
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        vals = []
        while head != None:
            vals.append(head.val)
            head = head.next
        for i in range(len(vals) // k):
            vals[i * k:i * k + k] = vals[i * k:i * k + k][::-1]
        head = ListNode(0)
        cur = head
        for val in vals:
            cur.next = ListNode(val)
            cur = cur.next
        return head.next

