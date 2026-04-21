# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # That means for every node:
        # everything in the left subtree is smaller
        # everything in the right subtree is larger
        # Not just the children.
        # Everything. All descendants.
        # BFS (level by level)
        # DFS (go deep into subtrees)
        def dfs(node, low, high):
            if not node:
                return True  # empty subtree is valid
            
            if not (low < node.val < high):
                return False  # violates BST rule
            
            return (
                dfs(node.left, low, node.val) and
                dfs(node.right, node.val, high)
            )
        
        return dfs(root, float('-inf'), float('inf'))

        
        