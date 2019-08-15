
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        cur = [root]
        while (cur):
            node_pre = None
            next_level = []
            for i in range(len(cur)):
                node = cur[i]
                # 下一个没有就是null
                if node_pre: node_pre.next = node
                node_pre = node
                if node.left or node.right:
                    next_level.append(node.left)
                    next_level.append(node.right)
            cur = next_level
        return root
