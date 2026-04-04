class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return len(self._items) == 0

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()

    def peek(self):
        if not self.is_empty():
            return self._items[-1]

    def __len__(self):
        return len(self._items)



class MyQueue(object):

    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.push(x)

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        
        return self.stack_out.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()