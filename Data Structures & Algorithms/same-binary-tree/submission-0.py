# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Two trees are the same if:
        # 1) Their root values are equal
        # 2) Their left subtrees are the same
        # 3) Their right subtrees are the same

        # If both nodes exist but their values are different,
        # the trees are not the same
        if p and q and p.val != q.val:
            return False
        # If p is None, then q must also be None for the trees to be the same
        if p == None:
            return q == None
        # If q is None, then p must also be None for the trees to be the same
        if q == None:
            return p == None
        # Recursively check:
        # - left subtrees are the same
        # - right subtrees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        