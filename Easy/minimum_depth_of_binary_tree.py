# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.__iterativeMin(root)

    def __iterativeMin(self, tree: TreeNode) -> int:
        if not tree:
            return 0

        queue = deque([(tree, 1)])
        while queue:
            node, dist = queue.popleft()

            if not node.left and not node.right:
                return dist

            if node.left:
                queue.append((node.left, dist+1))

            if node.right:
                queue.append((node.right, dist+1))
