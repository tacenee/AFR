# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, node):
        # write code here
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        self.in_stack.append(node)

    def pop(self):
        # return xx
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        if len(self.out_stack) > 0:
            return self.out_stack.pop()
