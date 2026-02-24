# Data Structures Roadmap & Reference

This document provides an overview of all data structures implemented in this repository, their properties, use cases, and complexity analysis.

## Table of Contents
1. [Core Structures](#core-structures)
2. [Advanced Structures](#advanced-structures)
3. [Quick Reference](#quick-reference)
4. [When to Use](#when-to-use)

---

## Core Structures

### Arrays
**Files**: `data_structures/{python,java}/arrays/`

**Description**: Collection of elements stored in contiguous memory, accessed via index.

**Core Operations**:
- Access: O(1)
- Search: O(n)
- Insert: O(n)
- Delete: O(n)

**Use Cases**: Storing sequential data, random access needed, cache locality important

### Linked Lists
**Files**: `data_structures/{python,java}/linked_lists/`

**Types Implemented**:
- Singly Linked List
- Doubly Linked List  
- Circular Linked List

**Core Operations**:
- Access: O(n)
- Search: O(n)
- Insert: O(1) (with pointer) or O(n)
- Delete: O(1) (with pointer) or O(n)

**Use Cases**: Dynamic memory allocation, frequent insertions/deletions, no random access needed

### Stacks
**Files**: `data_structures/{python,java}/stacks/`

**Description**: Last-In-First-Out (LIFO) data structure.

**Core Operations**:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)

**Use Cases**: Function call stack, expression evaluation, backtracking algorithms, undo functionality

### Queues
**Files**: `data_structures/{python,java}/queues/`

**Types Implemented**:
- Queue (FIFO)
- Deque (Double-ended queue)
- Priority Queue

**Core Operations**:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)

**Use Cases**: BFS traversal, task scheduling, message passing, level-order tree traversal

### Hash Tables
**Files**: `data_structures/{python,java}/hash_tables/`

**Collision Resolution Methods**:
- Chaining: Separate linked lists for each bucket
- Open Addressing: Probe for empty slot

**Core Operations** (average case):
- Insert: O(1)
- Delete: O(1)
- Search: O(1)

**Use Cases**: Fast lookups, caching, deduplication, counting frequencies

---

## Advanced Structures

### Trees
**Files**: `data_structures/{python,java}/trees/`

**Binary Tree**
- Complete binary tree stored implicitly or explicitly
- Operations: Insert O(n), Search O(n), Delete O(n)

**Binary Search Tree**
- All left descendants < node < all right descendants
- Average: Insert/Search/Delete O(log n)
- Worst: O(n) (unbalanced)

**AVL Tree**
- Self-balancing BST, height difference <= 1
- Guaranteed: Insert/Search/Delete O(log n)
- Slightly slower rotations than Red-Black

**Red-Black Tree**
- Self-balancing BST with color property
- Guaranteed: Insert/Search/Delete O(log n)
- Faster insertions than AVL

**Use Cases**: 
- BST: When balanced insertions/deletions needed
- AVL: Frequent searches on relatively static data
- RB: Frequent insertions/deletions (used in TreeMap/TreeSet)

### Specialized Trees
**Files**: `data_structures/{python,java}/trees/`

**Trie**
- Tree for storing strings with shared prefixes
- Insert/Search: O(m) where m = string length
- Space: O(ALPHABET_SIZE * N) where N = number of nodes
- Use: Autocomplete, spell checking, IP routing

**Segment Tree**
- Tree for range queries and point updates
- Build: O(n)
- Query: O(log n)
- Update: O(log n)
- Use: Range sum/min/max queries, interval updates

**Fenwick Tree (Binary Indexed Tree)**
- Efficient range queries and updates
- Query: O(log n)
- Update: O(log n)
- Space: O(n)
- Use: Prefix sum queries, point updates

### Heaps
**Files**: `data_structures/{python,java}/heaps/`

**Types**: Min-Heap, Max-Heap

**Core Operations**:
- Insert: O(log n)
- Delete Min/Max: O(log n)
- Get Min/Max: O(1)
- Heapify: O(n)

**Use Cases**: Priority queues, heap sort, finding k-largest/smallest elements

### Graphs
**Files**: `data_structures/{python,java}/graphs/`

**Representation Methods**:
- Adjacency List: O(V + E) space, good for sparse graphs
- Adjacency Matrix: O(V²) space, good for dense graphs

**Special Structure - Union-Find (Disjoint Set)**:
- Efficient set union and find operations
- Operations: O(α(n)) ≈ O(1) amortized with path compression
- Use: Cycle detection, connected components, Kruskal's MST

---

## Quick Reference

### Time Complexity Comparison

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| Stack | - | O(n) | O(1) | O(1) | O(n) |
| Queue | - | O(n) | O(1) | O(1) | O(n) |
| Hash Table | - | O(1)** | O(1)** | O(1)** | O(n) |
| BST | O(log n)* | O(log n)* | O(log n)* | O(log n)* | O(n) |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Red-Black | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | - | - | O(log n) | O(log n) | O(n) |
| Trie | - | O(m) | O(m) | O(m) | O(ALPHABET×N) |
| Union-Find | - | O(α(n)) | O(α(n)) | - | O(n) |

*With pointer
**Average case; worst case O(n) with poor hash function

---

## When to Use

### Choose Array if:
- You need fast random access
- Data size is known and fixed
- Memory is limited (compact storage)
- Cache locality is important

### Choose Linked List if:
- Frequent insertions/deletions at beginning
- Memory must be allocated dynamically
- Size changes significantly
- No random access needed

### Choose Hash Table if:
- Fast lookups are critical
- Insertions/deletions are frequent
- Order doesn't matter
- Memory space isn't severely limited

### Choose Tree if:
- Data is naturally hierarchical
- Range queries needed
- Sorted order important
- Balanced operations needed (AVL/RB-tree)

### Choose Heap if:
- Priority-based processing needed
- Finding min/max efficiently required
- Partial ordering sufficient

### Choose Trie if:
- String prefix matching needed
- Auto-complete functionality required
- Many strings with common prefixes

### Choose Graph if:
- Relationships between entities important
- Pathfinding needed
- Network/connectivity analysis required

---

## Implementation Tips

1. **Test edge cases**: Empty structures, single element, duplicates
2. **Understand space-time tradeoffs**: Hash tables trade space for time
3. **Consider memory access patterns**: Arrays have better cache locality
4. **Use appropriate balancing**: Unbalanced trees degrade to O(n)
5. **Profile your use case**: Theory and practice can differ significantly

