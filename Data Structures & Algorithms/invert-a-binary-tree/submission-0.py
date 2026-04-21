# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root and root.left:
            self.invertTree(root.left)
        if root and root.right:
            self.invertTree(root.right)

        if root:
            tmpl = root.left
            tmpr = root.right
            root.left = tmpr
            root.right = tmpl

        return root
        