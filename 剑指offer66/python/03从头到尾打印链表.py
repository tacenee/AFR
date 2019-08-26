# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        # pre = None
        # while listNode:
        #     cur = listNode
        #     next_node = listNode.next
        #     listNode.next = pre
        #     pre = cur
        #     listNode = next_node
        # return pre
        stack = []
        while listNode:
            stack.append(listNode.val)
            listNode = listNode.next
        return stack[::-1]
