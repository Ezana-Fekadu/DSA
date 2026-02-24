
"""Stack Implementation using List.

Operations:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)

Space Complexity: O(n)
"""

from typing import Any, List, Optional


class Stack:
    """Stack using list backend."""
    
    def __init__(self):
        """Initialize empty stack."""
        self._items: List[Any] = []
    
    def push(self, value: Any) -> None:
        """Push element. Time: O(1)"""
        self._items.append(value)
    
    def pop(self) -> Any:
        """Pop element. Time: O(1)"""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()
    
    def peek(self) -> Any:
        """Peek top element. Time: O(1)"""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]
    
    def is_empty(self) -> bool:
        """Check if empty. Time: O(1)"""
        return len(self._items) == 0
    
    def size(self) -> int:
        """Get size. Time: O(1)"""
        return len(self._items)
    
    def __str__(self) -> str:
        """String representation."""
        return f"Stack({self._items})"


if __name__ == "__main__":
    print("Test 1: Basic operations")
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Stack: {stack}")
    
    print("\nTest 2: Pop and peek")
    print(f"Peek: {stack.peek()}")
    print(f"Pop: {stack.pop()}")
    print(f"Stack after pop: {stack}")
    
    print("\nTest 3: Empty check")
    while not stack.is_empty():
        print(f"Popping: {stack.pop()}")
    print(f"Is empty: {stack.is_empty()}")
