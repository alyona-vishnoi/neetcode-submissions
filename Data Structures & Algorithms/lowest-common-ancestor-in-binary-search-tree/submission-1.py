# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # find lowest node st, p and q are decendents to the node or p and q are that node

        # if p and q are in diff subtrees then root is the LCA
        # else we can recurse
        # what if p is ancestor of q or vice versa

        if (p.val < root.val and q.val > root.val) or \
         (p.val > root.val and q.val < root.val) or \
         (p.val == root.val or q.val == root.val):
            return root

        else:
            if p.val < root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return self.lowestCommonAncestor(root.right, p, q)



        