# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        return self.__iterativeMaxDepth(root)


    def __recursiveMaxDepth(self, tree: TreeNode) -> int:
        if not tree:
            return 0

        leftHeight = self.__recursiveMaxDepth(tree.left)
        rightHeight = self.__recursiveMaxDepth(tree.right)
        
        return max(leftHeight, rightHeight)+1


    def __iterativeMaxDepth(self, tree: TreeNode) -> int:
        if not tree:
            return 0

        queue = deque()
        queue.append(tree)
        height = 0

        while True:
            
            nodeCount = len(queue)
            if nodeCount == 0:
                return height

            height+=1

            while nodeCount:

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                nodeCount-=1

