class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        point = root
        while point:
            # 通过二叉树左树小右树大性质判断根节点
            if p.val > point.val and q.val > point.val:
                point = point.right
            elif p.val < point.val and q.val < point.val:
                point = point.left
            else:
                return point