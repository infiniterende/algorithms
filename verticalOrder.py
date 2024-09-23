# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        res = []
        while queue:
            size = len(queue)
            for _ in range(size):
                node, offset = queue.popleft()
                res.append((node.val, offset))
                if node.left:
                    queue.append((node.left, offset-1))
                if node.right:
                    queue.append((node.right, offset+1))

        res.sort(key=lambda x: x[1])
        nodes = defaultdict(list)
        for node, offset in res:
            nodes[offset].append(node)

        return nodes.values()
