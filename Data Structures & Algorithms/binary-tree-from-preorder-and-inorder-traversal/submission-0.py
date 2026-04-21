# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root -> left -> right
        # in order: left -> root -> right
        if not preorder or not inorder:
            return None

        # 1. root is first element of preorder
        root_val = preorder[0]
        root = TreeNode(root_val)

        # 2. find root in inorder
        mid = inorder.index(root_val)
        # returns the position (index)
        # where that value appears in the inorder list

        # 3. split inorder
        left_inorder = inorder[:mid] # left subtree
        right_inorder = inorder[mid + 1:] # right subtree

        # 4. split preorder using size of left subtree
        left_preorder = preorder[1 : 1 + len(left_inorder)]
        right_preorder = preorder[1 + len(left_inorder):]

        # 5. recurse
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root