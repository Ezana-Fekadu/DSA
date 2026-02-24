# DSA – Data Structures and Algorithms in Python and Java

This repository is a **comprehensive reference** of core data structures and algorithms that computer science students and graduates are expected to know. It contains **clean, well-documented implementations** in both Python and Java, organized by topic with best practices throughout.

## Features

✅ **Complete Coverage**: All essential DSA topics for interview preparation  
✅ **Dual Language**: Implementations in both Python and Java  
✅ **Well-Documented**: Complexity analysis, docstrings, and Javadoc  
✅ **Examples Included**: Runnable demo code in every implementation  
✅ **Best Practices**: PEP 8 (Python), Google Style Guide (Java)  
✅ **Educational Focus**: Clear, understandable code optimized for learning  

## Repository Structure

```
DSA/
├── data_structures/       # Data structure implementations
│   ├── python/           # Python implementations
│   │   ├── arrays/
│   │   ├── linked_lists/
│   │   ├── stacks/
│   │   ├── queues/
│   │   ├── hash_tables/
│   │   ├── trees/
│   │   ├── heaps/
│   │   └── graphs/
│   └── java/             # Java implementations
│       ├── arrays/
│       ├── linked_lists/
│       ├── stacks/
│       ├── queues/
│       ├── hash_tables/
│       ├── trees/
│       ├── heaps/
│       └── graphs/
├── algorithms/           # Algorithm implementations
│   ├── python/           # Python implementations
│   │   ├── searching/
│   │   ├── sorting/
│   │   ├── recursion_divide_conquer/
│   │   ├── greedy/
│   │   ├── dynamic_programming/
│   │   ├── graph_algorithms/
│   │   ├── string_algorithms/
│   │   └── math_number_theory/
│   └── java/             # Java implementations
│       ├── searching/
│       ├── sorting/
│       ├── recursion_divide_conquer/
│       ├── greedy/
│       ├── dynamic_programming/
│       ├── graph_algorithms/
│       ├── string_algorithms/
│       └── math_number_theory/
├── docs/                 # Documentation
│   ├── data_structures.md
│   ├── algorithms.md
│   └── contribution_guide.md
├── README.md
├── LICENSE
└── .gitignore
```

## Data Structures Covered

### Core Structures
- **Arrays**: Dynamic arrays, matrix operations
- **Linked Lists**: Singly, doubly, and circular linked lists
- **Stacks**: Array-based and linked list implementations
- **Queues**: Queue, deque, and priority queue implementations
- **Hash Tables**: Chaining and open addressing collision resolution

### Advanced Structures
- **Trees**: Binary tree, Binary Search Tree, AVL Tree, Red-Black Tree
- **Specialized Trees**: Segment Tree, Fenwick Tree (Binary Indexed Tree), Trie
- **Heaps**: Min-heap, max-heap, heap operations
- **Graphs**: Adjacency list, adjacency matrix, union-find (disjoint set)

## Algorithms Covered

### Fundamental
- **Searching**: Linear search, binary search
- **Sorting**: Bubble, selection, insertion, merge, quick, heap, counting, radix
- **Recursion & Divide-and-Conquer**: Recursion basics, quickselect, closest pair

### Optimization & Design Paradigms
- **Greedy**: Interval scheduling, fractional knapsack, Huffman coding
- **Dynamic Programming**: Fibonacci, 0-1 knapsack, LCS, LIS, coin change

### Graph Algorithms
- **Traversal**: BFS, DFS, topological sort (Kahn & DFS-based)
- **Shortest Paths**: Dijkstra, Bellman-Ford, Floyd-Warshall
- **Minimum Spanning Tree**: Kruskal, Prim
- **Advanced**: Strongly connected components (Kosaraju)

### String & Math
- **String Matching**: Naive search, KMP, Rabin-Karp
- **Number Theory**: GCD (Euclidean), Sieve of Eratosthenes, fast exponentiation

## Getting Started

### Prerequisites
- **Python 3.11+** (no external dependencies required)
- **Java 17+** (compile with `javac`, run with `java`)

### Running Examples

**Python:**
```bash
# Navigate to a data structure or algorithm
cd data_structures/python/linked_lists

# Run the implementation directly
python3 singly_linked_list.py
```

**Java:**
```bash
# Navigate to a data structure or algorithm
cd data_structures/java/linked_lists

# Compile
javac SinglyLinkedList.java

# Run
java SinglyLinkedList
```

## Code Quality Standards

### Python
- ✅ PEP 8 compliant
- ✅ Type hints included
- ✅ Module-level docstrings
- ✅ Clear variable naming
- ✅ Example usage in `if __name__ == "__main__":` blocks

### Java
- ✅ Google Java Style Guide compliant
- ✅ One public class per file
- ✅ Comprehensive Javadoc comments
- ✅ Main method for demo execution
- ✅ Clear method documentation with complexity

### All Implementations
- ✅ Time and space complexity documented
- ✅ Clear comments explaining tricky logic
- ✅ Minimal dependencies (no external libraries)
- ✅ Consistent naming conventions

## Example Implementation Format

Each implementation follows this template:

```python
"""
Data Structure/Algorithm Name

Description and purpose.

Operations & Complexity:
- Operation1: O(n) time, O(1) space
- Operation2: O(log n) time, O(1) space
"""

class ImplementationName:
    """Class documentation."""
    
    def __init__(self):
        """Initialize."""
        pass
    
    def operation(self, param):
        """Operation documentation with complexity."""
        pass

if __name__ == "__main__":
    # Example usage
    pass
```

## Documentation

For detailed information, see:
- [`docs/data_structures.md`](docs/data_structures.md) – DS roadmap and complexity analysis
- [`docs/algorithms.md`](docs/algorithms.md) – Algorithm roadmap and classifications
- [`docs/contribution_guide.md`](docs/contribution_guide.md) – Guidelines for contributing

## Learning Path

### Beginner
1. Arrays and basic operations
2. Linked lists (singly and doubly)
3. Stacks and queues
4. Linear and binary search
5. Basic sorting (bubble, insertion, selection)

### Intermediate
1. Hash tables and collision resolution
2. Binary search trees
3. Advanced sorting (merge, quick, heap)
4. BFS and DFS
5. Dynamic programming basics

### Advanced
1. Balanced trees (AVL, Red-Black)
2. Advanced graph algorithms (Dijkstra, Kruskal, Prim)
3. Complex DP problems
4. String matching algorithms
5. Specialized trees (segment trees, tries, Fenwick trees)

## Usage Tips

- **Study & Learn**: Read implementations with accompanying complexity analysis
- **Interview Prep**: Use this as a checklist for interview preparation
- **Quick Reference**: Find implementations quickly by topic
- **Code Templates**: Adapt implementations for competitive programming
- **Teaching**: Use as educational material or reference for teaching DSA

## Contributing

Contributions are welcome! Please see [`docs/contribution_guide.md`](docs/contribution_guide.md) for:
- Code style requirements
- Testing guidelines
- Documentation standards
- Pull request process

## License

This project is licensed under the MIT License – see [`LICENSE`](LICENSE) for details.

## Disclaimer

While we strive for accuracy, this repository is primarily for **educational purposes**. Always verify implementations for production use and ensure they meet your specific requirements.

## Support

If you find issues, have questions, or want to suggest improvements:
1. Check existing documentation in `docs/`
2. Review similar implementations for comparison
3. Open an issue with detailed information
4. Submit a pull request with improvements

---

**Happy Learning!** 🚀