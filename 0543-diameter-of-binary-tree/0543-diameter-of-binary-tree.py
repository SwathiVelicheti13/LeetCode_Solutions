# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxdiam = 0
        def diam(root):
            nonlocal maxdiam

            if root is None:
                return 0

            lh = diam(root.left)
            rh = diam(root.right)

            diameter = lh+rh

            maxdiam = max(maxdiam,diameter)

            return max(lh,rh)+1
        diam(root)
        return maxdiam  


        