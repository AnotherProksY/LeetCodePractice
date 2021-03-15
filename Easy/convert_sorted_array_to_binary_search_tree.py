# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.__recursiveTreeCreation(0, len(nums)-1, nums)


    def __recursiveTreeCreation(self, l, r, list) -> TreeNode:

        if l>r:
            return None

        mid = (l+r) // 2
        root = TreeNode(list[mid])
        root.left = self.__recursiveTreeCreation(l, mid-1, list)
        root.right = self.__recursiveTreeCreation(mid+1, r, list)

        return root

