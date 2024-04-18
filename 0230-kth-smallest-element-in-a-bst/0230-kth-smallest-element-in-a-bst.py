# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        res = None
        def helper(root,k):
            nonlocal count,res
            """
            :type root: TreeNode
            :type k: int
            :rtype: int
            """
            if root is None:
                return

            helper(root.left,k)

            count+=1

            if count == k:
                res = root.val
                return
            helper(root.right,k)
        helper(root,k)
        return res
        