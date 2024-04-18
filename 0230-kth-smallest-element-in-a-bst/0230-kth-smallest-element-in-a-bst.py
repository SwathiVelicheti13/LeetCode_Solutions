# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        curr = root
        
        while curr:
            if curr.left is None:
                k = k-1
                if k == 0:
                    return curr.val
                curr = curr.right
                
            else:
                pred = curr.left
                
                while pred.right and pred.right!=curr:
                    pred = pred.right
                    
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right=None
                    k = k-1
                    if k == 0:
                        return curr.val
                    curr=curr.right
        return None
        