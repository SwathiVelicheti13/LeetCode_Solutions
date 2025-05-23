# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return 

        root.left,root.right = root.right,root.left

        # INCASE NULL VALUES NOT ALLOWED
        # if root.left and root.right:
        #     root.left,root.right = root.right,root.left

        # elif root.left:
        #     root.right = root.left
        
        # elif root.right:
        #     root.left = root.right

        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
        