# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while (root != None):
            if root.left:
                most_left = root.left
                while most_left.right:most_left = most_left.right
                most_left.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return
