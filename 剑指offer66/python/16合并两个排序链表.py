# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(0)
        head = dummy
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                dummy.next = pHead1
                pHead1 = pHead1.next
            else:
                dummy.next = pHead2
                pHead2 = pHead2.next
            dummy = dummy.next
        if pHead2:
            dummy.next = pHead2
        if pHead1:
            dummy.next = pHead1
        return head.next