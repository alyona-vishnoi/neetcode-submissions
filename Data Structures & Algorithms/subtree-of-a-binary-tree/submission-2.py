# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val != q.val:
            return False
        if p == None:
            return q == None
        if q == None:
            return p == None
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot == None:
            return True
        if root == None:
            return False

        if isSameTree(root, subRoot):
            return True
        else:
           return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
        
        