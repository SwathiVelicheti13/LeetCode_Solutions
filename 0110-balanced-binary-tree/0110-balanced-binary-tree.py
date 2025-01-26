# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def isBalance(root):
            if root is None:
                return 0

            lh = isBalance(root.left)
            rh = isBalance(root.right)

            if lh == -1 or rh == -1 or abs(lh-rh)>1:
                return -1
        
            return max(lh,rh)+1

        return isBalance(root)>0

    





        