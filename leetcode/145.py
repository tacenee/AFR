def postorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    ret = []
    def helper(root):
        if not root:return
        helper(root.left)
        helper(root.right)
        ret.append(root.val)
    helper(root)
    return ret