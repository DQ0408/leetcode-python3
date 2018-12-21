# -*- coding: utf-8 -*-
"""
Created on 2018/12/17 23:10
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        link_list = []
        while head != None:
            link_list.append(head.val)
            head = head.next
        link_list.pop(-n)
        if len(link_list)==0:
            return None
        head = ListNode(int(link_list[0]))
        cur = head
        for i, num in enumerate(link_list[1:]):
            cur.next = ListNode(int(num))
            cur = cur.next
        return head



# if __name__ == "__main__":
#     s = Solution()
#     head0 = s.get_list(32242321680068040)
#     # print(head0)
#     h = s.removeNthFromEnd(head0, 17)
#     # print(h)
