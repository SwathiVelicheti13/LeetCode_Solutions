# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def helper(root):
            nonlocal maxDiam
            if root is None:
                return 0

            lh = helper(root.left)
            rh = helper(root.right)
            
            diam = lh+rh
            maxDiam = max(maxDiam, diam)
           
            return 1+max(lh,rh)
        helper(root)
        return maxDiam
        