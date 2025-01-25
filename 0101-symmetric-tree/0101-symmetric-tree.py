# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        rl = root.left
        rr = root.right

        def Symmetric(rl,rr):
            if rl is None and rr is None:
                return True
            
            if rl is None or rr is None:
                return False
                
            return rl.val == rr.val and Symmetric(rl.left,rr.right) and Symmetric(rl.right,rr.left)

    
        return Symmetric(root.left,root.right)

        