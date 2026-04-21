# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # my guess is i want to keep track of visited.
        # if i visit twice then it has a cycle.
        # naive sol is hashset

        visited = set()

        curr = head
        while curr:
            if curr not in visited:
                visited.add(curr)
            else:
                return True
            curr = curr.next
        return False
        