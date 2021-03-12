# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.__checkTwoNodes(root.left, root.right)

    def __checkTwoNodes(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        elif not a or not b:
            return False
        else:
            return a.val == b.val and self.__checkTwoNodes(a.left, b.right) and self.__checkTwoNodes(a.right, b.left)
