# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # 判断B树是不是A树的子结构
        flag = False
        if not pRoot2: return False
        if not pRoot1 and pRoot2: return False
        if pRoot1.val == pRoot2.val:
            flag = self.helper(pRoot1, pRoot2)
        # 对比的是节点的值是否相同，一棵树上面可能有数值相同的节点
        return flag or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def helper(self, node1, node2):
        if not node2: return True
        if not node1 and node2: return False
        if node1.val == node2.val:
            return self.helper(node1.left, node2.left) and self.helper(node1.right, node2.right)
        return False
