class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        return (self.head == None and self.tail == None)

    def append(self, value: int) -> None:
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
        else:
            new = Node(value)
            self.head.next = new
            new.prev = self.head
            self.head = new

    def appendleft(self, value: int) -> None:
        if self.isEmpty():
            self.append(value)
        else:
            new = Node(value)
            new.next = self.tail
            self.tail.prev = new
            self.tail = new

    def pop(self) -> int:
        if self.isEmpty(): return -1
        else:
            old_head = self.head
            result = old_head.val
            if old_head.prev:
                self.head = old_head.prev
                self.head.next = None
                old_head.prev = None
            else:
                self.head = None
                self.tail = None 
            return result 

    def popleft(self) -> int:
       if self.isEmpty(): return -1
       else:
            result = self.tail.val
            old_tail = self.tail
            if old_tail.next:
                self.tail = old_tail.next
                self.tail.prev = None
                old_tail.next = None
            else:
                self.head = None
                self.tail = None
            return result
 