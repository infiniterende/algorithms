def longestConseuctive(root):

    def dfs(node, parent, currLen):
        if not node:
            return currLen
        consecutive = node.val - parent == 1
        currLen = currLen + 1 if consecutive else 1
        return max(currLen, dfs(node.left, node.val, currLen), dfs(node.right, node.val, currLen))

    return dfs(root, root.val, 0)
