# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # initially i would think of travesing the list in reverse
        # can try using fast and slow pointers
        dummy = ListNode()
        dummy.next = head

        slow = dummy # slow is prev of node to remove
        fast = head

        while n > 0 and fast:
            fast = fast.next
            n -= 1
        # make fast pointer go till nth node
        # gap between slow and fast is n

        while fast: # make fast go till end
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next # remove node

        return dummy.next

        



        