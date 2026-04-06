class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self.front is None

    def add(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self._size += 1

    def pop(self):
        if not self.is_empty():
            val = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self._size -= 1
            return val

    def peek(self):
        if not self.is_empty():
            return self.front.value

    def __len__(self):
        return self._size

class MyStack(object):
    def __init__(self):
        self.q = Queue()

    def push(self, x):
        self.q.add(x)
        for _ in range(len(self.q) - 1):
            self.q.add(self.q.pop())

    def pop(self):
        return self.q.pop()

    def top(self):
        return self.q.peek()

    def empty(self):
        return self.q.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
    