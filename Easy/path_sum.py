# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.targetSum = targetSum
        self.path_sum = self.__iterativePath(root)
        if self.path_sum:
            return self.path_sum == self.targetSum
        else:
            return False

    def __iterativePath(self, tree: TreeNode) -> int:
        if not tree:
            return 0

        queue = deque([(tree, tree.val)])
        while queue:
            node, val = queue.popleft()

            if not node.left and not node.right:
                if not queue:
                    return val
                else:
                    if val == self.targetSum:
                        return val
                    else:
                        continue

            if node.left:
                left_sum = val + node.left.val

                if left_sum <= self.targetSum:
                    queue.append((node.left, left_sum))

            if node.right:
                right_sum = val + node.right.val

                if right_sum <= self.targetSum:
                    queue.append((node.right, right_sum))
