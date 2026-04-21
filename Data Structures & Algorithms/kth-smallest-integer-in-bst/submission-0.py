# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def in_order_traversal(node):
            if node is None or len(values) == k:
                return
            
            # left
            in_order_traversal(node.left)
            
            # visit
            if len(values) < k:
                values.append(node.val)
            
            # right
            in_order_traversal(node.right)

        in_order_traversal(root)
        return values[k - 1]



