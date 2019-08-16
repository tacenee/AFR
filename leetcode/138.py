class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head: 'Node') -> 'Node':
    lookup = {}

    def dfs(node):
        if not node: return None
        if node in lookup:
            return lookup[node]
        clone = Node(node.val, None, None)
        lookup[node] = clone
        clone.random = dfs(node.random)
        clone.next = dfs(node.next)
        return clone
    return dfs(head)

