# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def helper(node, nums):
            if not node: return
            helper(node.left, nums)
            nums.append(node.val)
            helper(node.right, nums)

        nums = []
        helper(root, nums)
        return nums[k - 1]
