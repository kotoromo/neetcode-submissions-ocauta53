class MyStack:

    def __init__(self):
        self.is_q1 = True
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        if not self.is_q1: 
            self.q1.insert(0, x)
            self.is_q1 = True
        else: 
            self.q2.insert(0, x)
            self.is_q1 = False

    def pop(self) -> int:
        if self.is_q1:
            self.is_q1 = False
            return self.q1.pop(0)
        else:
            self.is_q1 = True
            return self.q2.pop(0)

    def top(self) -> int:
        if self.q1 and self.is_q1: return self.q1[0]
        elif self.q2 and not self.is_q1: return self.q2[0]

    def empty(self) -> bool:
        if self.is_q1:
            return len(self.q1) == 0
        else:
            return len(self.q2) == 0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()