# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        maxsum = 0
        def Tilt(root):
            nonlocal maxsum

            if root is None:
                return 0
            
            lsum = Tilt(root.left)
            rsum = Tilt(root.right)
            sum1 = abs(lsum-rsum)
            maxsum+=sum1
            return root.val+lsum+rsum
        Tilt(root)
        return maxsum