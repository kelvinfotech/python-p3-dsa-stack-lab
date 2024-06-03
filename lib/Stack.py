class Stack:
    def __init__(self, items=None, limit=100):
        """Initialize the stack with optional items and a size limit"""
        if items is None:
            items = []
        self.items = items[:limit]
        self.limit = limit

    def isEmpty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack if it is not full"""
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        """Pop an item off the stack and return it, or return None if the stack is empty"""
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        """Return the top item from the stack without removing it"""
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        """Return the size of the stack"""
        return len(self.items)

    def full(self):
        """Check if the stack is full"""
        return len(self.items) == self.limit

    def search(self, target):
        """Search for the target in the stack and return its position from the top (0-based index)"""
        try:
            return len(self.items) - self.items.index(target) - 1
        except ValueError:
            return -1