from typing import Union

class ListNode:
    def __init__(self, value : int, next=None):
        self.value = value
        self.next = next
    def __str__(self) -> str:
        return "({} -> {})".format(self.value, self.next.value if self.next else None)

class LinkedList:
    
    def __init__(self):
        self.head : Union[ListNode, None] = None
        self.tail : Union[ListNode, None] = None
    
    def get(self, index: int) -> int:
        """
            Return the value of the i-th node (0 indexed)
            If the index is out of bounds returns -1

            index : int - The index to retrieve.

            returns the value at the given index, -1 if the
            index is out of bounds.

            raises RuntimeError on error
        """
        try:
            result : Union[int, None] = None
            ptr : Union[ListNode, None] = self.head
            curr_idx = 0
            while ptr and not result:
                if curr_idx == index: 
                    result = ptr.value
                    break
                else: 
                    curr_idx += 1
                    ptr = ptr.next
            return result or -1
        except Exception:
            raise RuntimeError("Unhandled case. Input {}", index)

    def insertHead(self, val: int) -> None:
        """
            Inserts a node with the given value at the head of the list.

            val : int - Value to insert at the head of the list.

            returns None

            raises RuntimeError on error
        """
        try:
            old_head_ptr = self.head
            self.head = ListNode(val)
            self.head.next = old_head_ptr
        except Exception:
            raise RuntimeError("Unhandled case. Input {}", val)

    def insertTail(self, val: int) -> None:
        """
            Inserts a node with the given value at the tail of the list.

            val : int - Value to insert at the tail of the list.

            returns None

            raises RuntimeError on error
        """
        try:
            ptr : Union[ListNode, None] = self.tail or self.head
            
            # Case 1: No item in list
            if not ptr:
                return self.insertHead(val)
            # Case 2: No tail
            elif not self.tail:
                while ptr and ptr.next:
                    ptr = ptr.next
                self.tail = ptr
            # Case 3: tail exists
            if ptr and not ptr.next:
                self.tail = ListNode(val)
                ptr.next = self.tail
            else:
                raise Exception
        except Exception:
            raise RuntimeError("Unhandled case. Input {}".format(val))

    def remove(self, index: int) -> bool:
        """
            Removes the node at the given index (0-indexed).

            index : int - Index of the element to remove.

            returns false if the index is out of bounds, true otherwise.

            raises RuntimeError on error
        """
        try:
            ptr : Union[ListNode, None] = self.head
            prev_ptr : Union[ListNode, None] = None
            result : bool = False
            ptr_idx = 0
            
            if index == 0 and ptr:
                self.head = ptr.next
                result = True
            elif ptr:
                prev_ptr = ptr
                # Since not remove head case, advance one
                ptr = ptr.next
                ptr_idx += 1
                while prev_ptr and ptr:
                    if index == ptr_idx:
                        if not ptr.next:
                            prev_ptr.next = None
                            self.tail = prev_ptr
                        else:
                            prev_ptr.next = ptr.next
                        result = True
                        break
                    prev_ptr = ptr
                    ptr = ptr.next
                    ptr_idx += 1
            return result

        except Exception as e:
            raise RuntimeError("Unhandled case. Input {}".format(index))
    
    def getValues(self) -> List[int]:
        """
            Returns an array of all the values in the linked list,
            ordered from head to tail.
        """
        try:
            ptr : Union[None, ListNode] = self.head
            result = []
            while ptr:
                result.append(ptr.value)
                ptr = ptr.next
            return result
        except Exception:
            raise RuntimeError("Unhandled case.")
