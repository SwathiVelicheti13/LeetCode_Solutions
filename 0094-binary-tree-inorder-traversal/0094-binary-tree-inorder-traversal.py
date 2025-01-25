# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if root is None:
                return []
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
            
            return res
        return inorder(root)
        
        