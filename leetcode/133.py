class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


def cloneGraph(node):
    lookup = {}

    def dfs(node):
        if not node:return
        # 如果node已经在字典里，直接返回这个节点避免成环
        if node in lookup:
            return lookup[node]
        # 在lookup字典里记录这个节点
        clone = Node(node.val, [])
        lookup[node] = clone
        # 遍历这个node的neighbors，clone添加这些节点
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        return clone
    return dfs(node)
