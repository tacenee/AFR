# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not k:return
        if not head:return
        stack = []
        while head:
            stack.append(head)
            head = head.next
        if k>len(stack):return
        return stack[-k]
