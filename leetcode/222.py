class Solution(object):
    def countNodes(self, root):
        if not root: return 0
        hol = 0
        hor = 0
        curroot = root
        while curroot.left:
            hol += 1
            curroot = curroot.left
        curroot = root
        while curroot.right:
            hor += 1
            curroot = curroot.right
            while curroot.left:
                hor += 1
                curroot = curroot.left

        if hol == hor:
            highleft = 2 ** hol - 1
            highright = self.countNodes(root.right)
        else:
            highleft = self.countNodes(root.left)
            highright = 2 ** hor - 1
        return highright + highleft + 1
