# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        ret = []
        current = [root] 
        next_node = []
        level = False
        while current:
            cur = []
            for node in current:
                if not node:
                    continue
                cur.append(node.val)
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            if level:
                ret.append(cur[::-1])
            else:
                ret.append(cur)
            current, next_node = next_node, []
            level = not level
        return ret