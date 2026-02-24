# Linked Lists

Linked list implementations in Python.

## Overview
Linked lists are linear data structures where elements are not stored in contiguous memory locations. Each element (node) contains data and a reference (pointer) to the next node.

## Implementations

| File | Description | Time Complexity |
|------|-------------|----------------|
| [singly_linked_list.py](singly_linked_list.py) | Basic linked list | Insert: O(1) head, O(n) tail |

## When to Use
- Frequent insertions/deletions
- Dynamic size unknown
- No random access needed

## Key Operations
- **Insert at head**: O(1)
- **Insert at tail**: O(n)
- **Search**: O(n)
- **Delete**: O(n)
