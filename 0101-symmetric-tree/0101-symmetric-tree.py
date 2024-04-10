# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if root is None:
            return True
        return self.mirror(root.left, root.right)
    
    def mirror(self,left,right):
        if left is None and right is None:
            return True
        
        elif left is None or right is None:
            return False
        elif left is not None and right is not None:
            return left.val == right.val and self.mirror(left.left,right.right) and self.mirror(left.right,right.left)
        
            
        
        