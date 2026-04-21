# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bacially asking up to do a bfs
        # remember we want to go by level
        # also remember the queue trick!

        # init
        curr = root
        q = []
        if curr:
            q.append(curr)
        res = []
        curr_lvl = 0

        while q: # while the q is not empty
            res.append([])
            for _ in range(len(q)):
                # append every node at this level to res
                curr = q.pop(0)
                if curr:
                    res[curr_lvl].append(curr.val)
                # get each child for every node at this level
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            curr_lvl += 1

        return res




        