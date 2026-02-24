
"""Queue Implementation using List.

Operations:
- Enqueue: O(n) with list, O(1) with deque
- Dequeue: O(1)
- Peek: O(1)

Space Complexity: O(n)
"""

from typing import Any, Deque
from collections import deque


class Queue:
    """Queue using deque backend (O(1) operations)."""
    
    def __init__(self):
        """Initialize empty queue."""
        self._items: Deque[Any] = deque()
    
    def enqueue(self, value: Any) -> None:
        """Add element to queue. Time: O(1)"""
        self._items.append(value)
    
    def dequeue(self) -> Any:
        """Remove and return first element. Time: O(1)"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self._items.popleft()
    
    def peek(self) -> Any:
        """Get first element. Time: O(1)"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._items[0]
    
    def is_empty(self) -> bool:
        """Check if empty. Time: O(1)"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Get size. Time: O(1)"""
        return len(self._items)
    
    def __str__(self) -> str:
        """String representation."""
        return f"Queue({list(self._items)})"


if __name__ == "__main__":
    print("Test 1: Basic operations")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(f"Queue: {q}")
    
    print("\nTest 2: Dequeue")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Queue: {q}")
    
    print("\nTest 3: FIFO order")
    while not q.is_empty():
        print(f"Dequeue: {q.dequeue()}")
