
"""Singly Linked List Implementation.

Operations:
- Access: O(n)
- Search: O(n)
- Insert: O(1) (with pointer) or O(n)
- Delete: O(1) (with pointer) or O(n)

Space Complexity: O(n)
"""

from typing import Any, Optional


class Node:
    """Represents a node in the linked list."""
    
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[Node] = None


class SinglyLinkedList:
    """Singly linked list implementation."""
    
    def __init__(self):
        """Initialize empty linked list."""
        self.head: Optional[Node] = None
    
    def insert_at_head(self, data: Any) -> None:
        """Insert element at head. Time: O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_tail(self, data: Any) -> None:
        """Insert element at tail. Time: O(n)"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def search(self, data: Any) -> bool:
        """Search for element. Time: O(n)"""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False
    
    def delete(self, data: Any) -> bool:
        """Delete first occurrence. Time: O(n)"""
        if not self.head:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return True
            current = current.next
        return False
    
    def __str__(self) -> str:
        """String representation."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) or "Empty"


if __name__ == "__main__":
    print("Test 1: Basic operations")
    ll = SinglyLinkedList()
    ll.insert_at_tail(1)
    ll.insert_at_tail(2)
    ll.insert_at_tail(3)
    print(f"List: {ll}")
    
    print("\nTest 2: Insert at head")
    ll.insert_at_head(0)
    print(f"After insert at head: {ll}")
    
    print("\nTest 3: Search")
    print(f"Search 2: {ll.search(2)}")
    print(f"Search 5: {ll.search(5)}")
    
    print("\nTest 4: Delete")
    ll.delete(2)
    print(f"After delete 2: {ll}")
