# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Given the beginning of a singly linked list head, reverse the list, and return p
the new beginning of the list.

Input: head = [0,1,2,3]

Output: [3,2,1,0]


"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # For each node, take note of the previous node, create new head node and
        # s.t. its next is the old new head

        prev_node_ptr : Optional[ListNode] = None
        node_ptr : Optional[ListNode] = head
        new_head_ptr : Optional[ListNode] = None 

        while node_ptr:
            prev_node_ptr = node_ptr
            node_ptr = node_ptr.next
            new_head_ptr = ListNode(
                prev_node_ptr.val,
                new_head_ptr
            )
        
        return new_head_ptr