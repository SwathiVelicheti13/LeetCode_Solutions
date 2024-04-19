# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        first=middle=last=prev=None
        
        def inorder(root):
            nonlocal first, middle,last,prev
            if not root:
                return
            inorder(root.left)
            if prev is not None and root.val<prev.val:
                if first is None:
                    first = prev 
                    middle = root
                else:
                    last = root
                    
            prev = root
            
            inorder(root.right)

        inorder(root)
        if last:
            first.val,last.val = last.val,first.val
        else:
            first.val,middle.val = middle.val,first.val
        
        
        