class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
        self._size = 0

    def is_empty(self):
        return self.top_node is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top_node
        self.top_node = new_node
        self._size += 1

    def pop(self):
        if not self.is_empty():
            val = self.top_node.value
            self.top_node = self.top_node.next
            self._size -= 1
            return val

    def peek(self):
        if not self.is_empty():
            return self.top_node.value

    def __len__(self):
        return self._size

class MyQueue(object):
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def push(self, x):
        self.stack_in.push(x)

    def pop(self):
        self.peek()
        return self.stack_out.pop()

    def peek(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()

    def empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()