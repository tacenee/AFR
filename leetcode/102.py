# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root: return None
        ret = []
        current = [root]
        next_node = []
        level = True
        while current:
            cur = []
            if level:
                while current:
                    temp_node = current.pop()
                    cur.append(temp_node.val)
                    if temp_node.right: next_node.append(temp_node.right)
                    if temp_node.left: next_node.append(temp_node.left)
            else:
                for node in current:
                    cur.append(node.val)
                    if node.left: next_node.append(node.left)
                    if node.right: next_node.append(node.right)
            ret.append(cur)
            current, next_node = next_node, []
            level = not level

# class Solution:
#     def levelOrder(self, root: TreeNode) -> List[List[int]]:
#         if not root: return []
#         cur, nex, tmp, res = [root], [], [], []
#         while cur:
#             for r in cur:
#                 tmp.append(r.val)
#                 if r.left: nex.append(r.left)
#                 if r.right: nex.append(r.right)
#             res.append(tmp[:])
#             cur, nex, tmp = nex, [], []
#         return res
