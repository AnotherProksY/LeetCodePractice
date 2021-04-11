# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Iterative
        # self.targetSum = targetSum
        # self.path_sum = self.__iterativePath(root)
        # if self.path_sum:
        #     return self.path_sum == self.targetSum
        # else:
        #     return False
        
        # Recursive
        return self.__recursivePath(root, targetSum)

        
    def __recursivePath(self, tree: TreeNode, targetSum: int) -> bool:
        if not tree:
            return False

        if not tree.left and not tree.right and tree.val == targetSum:
            return True

        return self.hasPathSum(tree.left, targetSum - tree.val) or self.hasPathSum(tree.right, targetSum - tree.val)

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
                queue.append((node.left, left_sum))

            if node.right:
                right_sum = val + node.right.val
                queue.append((node.right, right_sum))
