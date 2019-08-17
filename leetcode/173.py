# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):

    def __init__(self, root: TreeNode):
        self.stack = []
        self.push_stack(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        #如果送出的结点有右节点，把这个节点所有的左节点添加进来
        tmp = self.stack.pop()
        if tmp.right:
            self.push_stack(tmp.right)
        return tmp.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)

    def push_stack(self, node):
        while node:
            self.stack.append(node)
            node = node.left



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
