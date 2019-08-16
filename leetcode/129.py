# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right:
            return root.val
        return self.bianli(root, [])

    def bianli(self, node, sumb):
        if not node: return 0
        if not node.left and not node.right:
            sumb.append(node.val)
            num = self.arrtonum(sumb)
            sumb.pop()
            return num
        else:
            sumb.append(node.val)
            num = self.bianli(node.left, sumb) + self.bianli(node.right, sumb)
            sumb.pop()
            return num

    def arrtonum(self, nums):
        num = 0
        for i in range(len(nums)):
            num += nums[i] * pow(10, len(nums) - i - 1)
        return num
