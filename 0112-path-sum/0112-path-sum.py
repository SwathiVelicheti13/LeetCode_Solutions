# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        
        targetSum = targetSum-root.val
            
        if self.hasPathSum(root.left,targetSum):
            return True
        
        if self.hasPathSum(root.right,targetSum):
            return True
        
        return False
            
        