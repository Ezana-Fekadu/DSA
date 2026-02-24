"""
Dynamic Array Implementation

A resizable array that grows when full, similar to Python's list.

Operations:
- Access: O(1)
- Search: O(n)
- Insert (at end): O(1) amortized
- Insert (at position): O(n)
- Delete: O(n)

Space Complexity: O(n)
"""

from typing import Any, List, Optional


class DynamicArray:
    """A resizable array with automatic capacity management."""
    
    def __init__(self, capacity: int = 10):
        """Initialize dynamic array with given capacity."""
        self.capacity = capacity
        self.size = 0
        self._items = [None] * capacity
    
    def _resize(self) -> None:
        """Double capacity and copy elements."""
        self.capacity *= 2
        new_items = [None] * self.capacity
        for i in range(self.size):
            new_items[i] = self._items[i]
        self._items = new_items
    
    def append(self, value: Any) -> None:
        """Add element to end of array.
        
        Time: O(1) amortized
        Space: O(1)
        """
        if self.size == self.capacity:
            self._resize()
        self._items[self.size] = value
        self.size += 1
    
    def get(self, index: int) -> Any:
        """Get element at index.
        
        Time: O(1)
        Space: O(1)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self._items[index]
    
    def set(self, index: int, value: Any) -> None:
        """Set element at index.
        
        Time: O(1)
        Space: O(1)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self._items[index] = value
    
    def remove_at(self, index: int) -> Any:
        """Remove and return element at index.
        
        Time: O(n)
        Space: O(1)
        """
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        removed = self._items[index]
        # Shift elements left
        for i in range(index, self.size - 1):
            self._items[i] = self._items[i + 1]
        self.size -= 1
        return removed
    
    def __len__(self) -> int:
        """Return size of array."""
        return self.size
    
    def __str__(self) -> str:
        """String representation."""
        items = [self._items[i] for i in range(self.size)]
        return str(items)


if __name__ == "__main__":
    # Test 1: Basic operations
    print("Test 1: Basic operations")
    arr = DynamicArray(2)  # Start with small capacity
    arr.append(1)
    arr.append(2)
    arr.append(3)  # This should trigger resize
    arr.append(4)
    print(f"Array: {arr}")
    print(f"Size: {len(arr)}, Capacity: {arr.capacity}")
    
    # Test 2: Indexing
    print("\nTest 2: Indexing")
    print(f"Element at index 0: {arr.get(0)}")
    print(f"Element at index 2: {arr.get(2)}")
    
    # Test 3: Removal
    print("\nTest 3: Removal")
    removed = arr.remove_at(1)
    print(f"Removed element: {removed}")
    print(f"Array after removal: {arr}")
    
    # Test 4: Edge cases
    print("\nTest 4: Edge cases")
    try:
        arr.get(100)
    except IndexError as e:
        print(f"Caught expected error: {e}")
