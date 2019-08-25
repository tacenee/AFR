class Solution:

    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        def recurse_tree(current_node):
            if not current_node:
                return False
            # 看左右分支上是否有我要的节点，有就为1
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q
            # mid保证 本身是不是目标节点 左右保证不是它自身，而是它的子结点
            if mid + left + right >= 2:
                self.ans = current_node
            # 保证这一条分支上有目标节点
            return mid or left or right

        recurse_tree(root)
        return self.ans
