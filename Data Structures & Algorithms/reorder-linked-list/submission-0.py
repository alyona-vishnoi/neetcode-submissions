# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first i want to have a reversed list
        # the issue is i only want to reverse the second half
        # then ill use fast and slow pointers
        if not head or not head.next:
            return
        
        # find middle:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # slow will be at middle
        # reverse second half / split
        prev = None
        curr = slow.next
        slow.next = None # split the first half
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # finally merge
        first, second = head, prev # head of reversed
        while second:
            nxt1 = first.next
            nxt2 = second.next

            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2
        return None
             








    

        result = ListNode()
        tortoise = head
        hare = head
        while hare:
            result = tortoise
            result.next = hare

            result = result.next.next

            tortoise = tortoise.next
            hare = hare.next.next

        return result.next






        