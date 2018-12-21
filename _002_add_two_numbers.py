# -*- coding: utf-8 -*-
"""
Created on 2018/12/02 16:28
@author: Sucre
@email: qian.dong.2018@gmail.com
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1 = self.get_number(l1)
        l2 = self.get_number(l2)
        output = self.get_list(l1 + l2)
        return output

    def get_number(self, linked_list):
        value = 0
        cnt = 0
        while not linked_list is None:
            value += linked_list.val * (10 ** cnt)
            linked_list = linked_list.next
            cnt += 1
        return value

    def get_list(self, value):
        value = str(value)
        value = value[::-1]
        head = ListNode(int(value[0]))
        cur = head
        for i, num in enumerate(value[1:]):
            cur.next = ListNode(int(num))
            cur = cur.next
        return head


if __name__ == "__main__":
    s = Solution()
    head0 = s.get_list(0)
    head1 = s.get_list(0)
    output = s.addTwoNumbers(head0, head1)
    print(output.next)
    v = s.get_number(output)
    print(v)
