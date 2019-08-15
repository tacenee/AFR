# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        ret = []

        def hasPathSum(root, ev, sum):
            if not root: return
            if root.val == sum and not root.left and not root.right:
                ev += [root.val]
                ret.append(ev)
                return
            hasPathSum(root.left, ev + [root.val], sum - root.val)
            hasPathSum(root.right, ev + [root.val], sum - root.val)

        hasPathSum(root, [], sum)
        return ret
        # res = []
        # if not root: return []
        # def helper(root,sum, tmp):
        #     if not root:
        #         return
        #     if not root.left and not root.right and sum - root.val == 0 :
        #         tmp += [root.val]
        #         res.append(tmp)
        #         return
        #     helper(root.left, sum - root.val, tmp + [root.val])
        #     helper(root.right, sum - root.val, tmp + [root.val])
        # helper(root, sum, [])
        # return res

