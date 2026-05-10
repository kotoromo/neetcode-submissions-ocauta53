# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, 
                      list1: Optional[ListNode], 
                      list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2: return list1
        elif list2 and not list1: return list2
        elif not (list1 and list2): return list1

        merged_ptr : Optional[ListNode] = None
        merged_head : Optional[ListNode] = None
        if list1.val <= list2.val:
            min_val = list1.val
            list1 = list1.next
        else:
            min_val = list2.val
            list2 = list2.next
        merged_head = ListNode(min_val)
        merged_ptr = merged_head

        while list1 and list2:
            if list1.val <= list2.val:
                min_val = list1.val
                list1 = list1.next
            else:
                min_val = list2.val
                list2 = list2.next
            merged_ptr.next = ListNode(min_val)
            merged_ptr = merged_ptr.next
        
        remaining_list : ListNode = list1 or list2
        while remaining_list:
            merged_ptr.next = ListNode(remaining_list.val)
            merged_ptr = merged_ptr.next
            remaining_list = remaining_list.next
        return merged_head