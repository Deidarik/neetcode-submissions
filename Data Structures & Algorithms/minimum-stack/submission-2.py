class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class minSupStack:
    def __init__(self):
        self.head = None

    def push(self, val: int) -> None: 
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> None:
        if self.head is None:
            return 
        self.head = self.head.next

    def top(self) -> int:
        if self.head is None:
            return 2**31 - 1
        return self.head.val

class MinStack:

    def __init__(self):
        self.head = None
        self.minss = minSupStack()

    def push(self, val: int) -> None: 
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.minss.push(min(self.minss.top(), new_node.val))

    def pop(self) -> None:
        if self.head is None:
            return 
        self.head = self.head.next
        self.minss.pop()

    def top(self) -> int:
        if self.head is None:
            return 2**31-1
        return self.head.val

    def getMin(self) -> int:
        return self.minss.top()
        
