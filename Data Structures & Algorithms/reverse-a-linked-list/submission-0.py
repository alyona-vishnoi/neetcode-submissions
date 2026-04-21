# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # basically we want to make next node point to previous node
        # curr node
        # next node
        # prev node
        
        # initialize 
        prev_node = None
        curr_node = head
        # while we havent reached end
        while curr_node:
            # store the next node so we dont lose it
            next_node = curr_node.next
            # make my next point to previous -> reversing it
            curr_node.next = prev_node

            # to move on to next elements...
            prev_node = curr_node
            curr_node = next_node

        # the tail becomes the head.
        return prev_node

