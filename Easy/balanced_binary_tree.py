class Solution:
    
    def __init__(self):
        self.ok = True
    
    def isBalanced(self, root: TreeNode) -> bool:
        self.__recursiveTreeCheck(root)
        return self.ok


    def __recursiveTreeCheck(self, tree: TreeNode) -> int:
        if tree and self.ok:
            l  = self.__recursiveTreeCheck(tree.left)
            r  = self.__recursiveTreeCheck(tree.right)

            if abs(l-r)>1:
                self.ok = False

            return 1+max(l,r)
            
        return 0
