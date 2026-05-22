# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rec(head)
    
    def rec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head

        # sps head : a -> b -> c
        reversed_list = self.rec(head.next)
        # reversed_list : c -> b -> null

        # move head to tail; since head.next is used for rec, then that's the tail of the rev list
        head.next.next = head
        head.next = None
        # reversed_list : c -> b -> a -> None
        head = reversed_list
        return head
