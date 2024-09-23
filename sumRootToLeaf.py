def sumNumbers(root):
    def dfs(node, pathSum):
        if node is None:
            return 0
        pathSum = 10 * pathSum + node.val
        if node.left is None and node.right is None:
            return pathSum
        return dfs(node.right, pathSum) + dfs(node.left, pathSum)
    return dfs(root, 0)

# O(N)
