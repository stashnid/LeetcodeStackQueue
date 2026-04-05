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


class FreqStack(object):
    def __init__(self):
        self.counts = {}
        self.stacks_by_frequency = {}
        self.record_frequency = 0

    def push(self, val):
        if val in self.counts:
            self.counts[val] = self.counts[val] + 1
        else:
            self.counts[val] = 1
            
        current_count = self.counts[val]
        
        if current_count > self.record_frequency:
            self.record_frequency = current_count
            
        if current_count not in self.stacks_by_frequency:
            self.stacks_by_frequency[current_count] = Stack()
            
        self.stacks_by_frequency[current_count].push(val)

    def pop(self):
        target_stack = self.stacks_by_frequency[self.record_frequency]
        number_to_remove = target_stack.pop()
        
        self.counts[number_to_remove] = self.counts[number_to_remove] - 1
        
        if target_stack.is_empty():
            self.record_frequency = self.record_frequency - 1
            
        return number_to_remove

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()