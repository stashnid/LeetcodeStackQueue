from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def is_empty(self):
        return len(self._items) == 0

    def add(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.popleft()

    def peek(self):
        if not self.is_empty():
            return self._items[0]

    def __len__(self):
        return len(self._items)


class MyStack(object):

    def __init__(self):
        self.q = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q.add(x)
        for _ in range(len(self.q) - 1):
            self.q.add(self.q.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.q.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.q.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.q.is_empty()

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
    