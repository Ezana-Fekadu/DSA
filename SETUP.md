# Setup & Getting Started

Quick guide to using this DSA repository.

## Structure Overview

This repository contains:
- **data_structures/**: Complete data structure implementations
  - `python/`: Python implementations with type hints
  - `java/`: Java implementations with Javadoc
- **algorithms/**: Core algorithm implementations
  - `python/`: Python algorithm implementations
  - `java/`: Java algorithm implementations  
- **docs/**: Comprehensive documentation
  - `data_structures.md`: DS guide and complexity reference
  - `algorithms.md`: Algorithm guide and roadmap
  - `contribution_guide.md`: How to contribute

## Running Examples

### Python
```bash
# Navigate to any Python file and run it
cd data_structures/python/linked_lists
python3 singly_linked_list.py

# Or run algorithms
cd algorithms/python/searching
python3 binary_search.py
```

### Java
```bash
# Navigate to any Java file, compile and run
cd data_structures/java/linked_lists
javac SinglyLinkedList.java
java SinglyLinkedList

# Or run algorithms
cd algorithms/java/searching
javac BinarySearch.java
java BinarySearch
```

## What's Implemented

### Data Structures (Both Python & Java)
- ✅ Arrays (Dynamic Array)
- ✅ Linked Lists (Singly Linked List)
- ✅ Stacks (List-based)
- ✅ Queues (Deque-based)
- ✅ Binary Search Trees
- Plus folder structure for: Hash Tables, Heaps, Graphs, Advanced Trees

### Algorithms (Both Python & Java)
- ✅ Binary Search (Iterative & Recursive)
- ✅ Merge Sort
- ✅ Quick Sort
- ✅ BFS & DFS (Graph Traversal)
- Plus folder structure for: Dynamic Programming, Greedy, String Algorithms, Math

## Next Steps

1. **Explore existing implementations**: Browse the completed files
2. **Add more implementations**: Use existing files as templates
3. **Add tests**: Create unit tests for your implementations
4. **Read documentation**: Check `docs/` for detailed guides
5. **Contribute**: Follow `docs/contribution_guide.md`

## File Naming Conventions

- **Python**: `snake_case.py` (e.g., `binary_search_tree.py`)
- **Java**: `PascalCase.java` (e.g., `BinarySearchTree.java`)
- **Folders**: `snake_case` (e.g., `dynamic_programming/`)

## Testing Your Code

Each implementation includes example usage in the `main` block:

**Python**:
```python
if __name__ == "__main__":
    # Test code here
    pass
```

**Java**:
```java
public static void main(String[] args) {
    // Test code here
}
```

## Common Commands

```bash
# Find all Python implementations
find . -name '*.py' -type f | grep -E '(data_structures|algorithms)'

# Find all Java implementations
find . -name '*.java' -type f | grep -E '(data_structures|algorithms)'

# Count implementations
find . -name '*.py' -type f | wc -l  # Python files
find . -name '*.java' -type f | wc -l  # Java files
```

## Learning Path

1. **Week 1-2**: Start with basic data structures (arrays, linked lists, stacks, queues)
2. **Week 3-4**: Move to trees (BST) and basic sorting
3. **Week 5-6**: Graph algorithms (BFS, DFS)
4. **Week 7-8**: Advanced algorithms (DP, Greedy)
5. **Week 9+**: Specialized structures and complex algorithms

For detailed learning paths, see `docs/algorithms.md` and `docs/data_structures.md`.
