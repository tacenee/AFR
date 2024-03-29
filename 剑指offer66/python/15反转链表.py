# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        while pHead:
            cur = pHead
            next_node = pHead.next
            pHead.next = pre
            pre = cur
            pHead = next_node
        return pre
