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
            self.record_frequency -= 1
            
        return number_to_remove

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()