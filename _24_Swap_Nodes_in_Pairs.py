# -*- coding: utf-8 -*-
"""
Created on 2018/12/19 10:16
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        vals = []
        while head!=None:
            vals.append(head.val)
            head=head.next
        for i in range(len(vals)//2):
            tmp = vals[i*2]
            vals[i * 2] = vals[i*2+1]
            vals[i*2+1] = tmp
        head = ListNode(0)
        cur = head
        for val in vals:
            cur.next = ListNode(val)
            cur = cur.next
        return head.next


