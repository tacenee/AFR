class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ret = []

    def helper(root):
        if not root: return
        ret.append(root.val)
        helper(root.left)
        helper(root.right)

    helper(root)
    return ret
