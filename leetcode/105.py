class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def buildTree(preorder, inorder):
    if not inorder:
        return None
    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])

    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
    # root.right = buildTree(preorder[])
    return root
