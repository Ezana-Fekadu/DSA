# Algorithms Roadmap & Reference

This document provides a comprehensive overview of all algorithms implemented in this repository, organized by category with complexity analysis and use cases.

## Table of Contents
1. [Searching](#searching)
2. [Sorting](#sorting)
3. [Recursion & Divide-and-Conquer](#recursion--divide-and-conquer)
4. [Greedy Algorithms](#greedy-algorithms)
5. [Dynamic Programming](#dynamic-programming)
6. [Graph Algorithms](#graph-algorithms)
7. [String Algorithms](#string-algorithms)
8. [Math & Number Theory](#math--number-theory)
9. [Complexity Reference](#complexity-reference)

---

## Searching

**Files**: `algorithms/{python,java}/searching/`

### Linear Search
- **Best Case**: O(1) - found at first position
- **Average Case**: O(n)
- **Worst Case**: O(n) - not found or at end
- **Space**: O(1)
- **Use**: Unsorted data, small datasets

### Binary Search
- **Prerequisite**: Sorted array
- **Best Case**: O(1)
- **Average Case**: O(log n)
- **Worst Case**: O(log n)
- **Space**: O(1) iterative, O(log n) recursive
- **Use**: Sorted data, large datasets, interview favorite

---

## Sorting

**Files**: `algorithms/{python,java}/sorting/`

| Algorithm | Best | Average | Worst | Space | Stable | In-Place |
|-----------|------|---------|-------|-------|--------|----------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |
| Counting Sort | O(n + k) | O(n + k) | O(n + k) | O(k) | Yes | No |
| Radix Sort | O(nk) | O(nk) | O(nk) | O(n + k) | Yes | No |

**Use Cases**:
- **Bubble/Selection**: Learning only, already sorted data
- **Insertion**: Small datasets, nearly sorted data
- **Merge**: Stability needed, external sorting
- **Quick**: General-purpose, cached-friendly
- **Heap**: Guaranteed O(n log n), space-limited
- **Counting/Radix**: Integer/small range sorting

---

## Recursion & Divide-and-Conquer

**Files**: `algorithms/{python,java}/recursion_divide_conquer/`

### Master Theorem
For T(n) = aT(n/b) + f(n):
- If f(n) ∈ O(n^(log_b(a) - ε)): T(n) = Θ(n^(log_b(a)))
- If f(n) ∈ Θ(n^(log_b(a))): T(n) = Θ(n^(log_b(a)) log n)
- If f(n) ∈ Ω(n^(log_b(a) + ε)): T(n) = Θ(f(n))

### Key Algorithms
- **Merge Sort**: O(n log n), stable
- **Quick Sort**: Average O(n log n), in-place
- **Quickselect**: Find kth element in O(n) average
- **Closest Pair**: 2D points in O(n log n)

---

## Greedy Algorithms

**Files**: `algorithms/{python,java}/greedy/`

### Characteristics
- Make locally optimal choice at each step
- Hope for globally optimal solution
- Proof of correctness often required
- Fast but doesn't always give optimal answer

### Implementations

**Interval Scheduling**
- Maximize non-overlapping intervals
- Time: O(n log n), Space: O(1)

**Fractional Knapsack**
- Maximize value with weight constraint
- Items can be divided
- Time: O(n log n), Space: O(1)

**Huffman Coding**
- Optimal variable-length prefix codes
- Time: O(n log n), Space: O(n)

---

## Dynamic Programming

**Files**: `algorithms/{python,java}/dynamic_programming/`

### Principles
1. **Optimal Substructure**: Optimal solution contains optimal subsolutions
2. **Overlapping Subproblems**: Same subproblems solved repeatedly
3. **Memoization** or **Tabulation**: Cache results to avoid recomputation

### Common Patterns

**1D DP**
- Fibonacci: O(n) time, O(n) or O(1) space
- Coin Change: O(n*amount)
- LIS (Longest Increasing Subsequence): O(n log n) with binary search

**2D DP**
- 0-1 Knapsack: O(n*W) time, O(n*W) space
- LCS (Longest Common Subsequence): O(m*n)
- Edit Distance (Levenshtein): O(m*n)

**DP on Strings/Sequences**
- LCS: Find longest common subsequence
- LIS: Find longest increasing subsequence
- Edit Distance: Minimum edits to transform string

---

## Graph Algorithms

**Files**: `algorithms/{python,java}/graph_algorithms/`

### Graph Traversal

**Breadth-First Search (BFS)**
- Time: O(V + E)
- Space: O(V)
- Use: Shortest path (unweighted), level-order

**Depth-First Search (DFS)**
- Time: O(V + E)
- Space: O(V) recursion stack
- Use: Topological sort, cycle detection, connected components

### Shortest Path

**Dijkstra's Algorithm**
- Prerequisite: Non-negative weights
- Time: O((V + E) log V) with binary heap
- Space: O(V)
- Use: GPS navigation, network routing

**Bellman-Ford**
- Time: O(V*E)
- Space: O(V)
- Use: Negative weights allowed, detects negative cycles

**Floyd-Warshall**
- Time: O(V³)
- Space: O(V²)
- Use: All-pairs shortest paths

### Minimum Spanning Tree

**Kruskal's Algorithm**
- Sort edges by weight, add if no cycle
- Time: O(E log E)
- Space: O(V + E)

**Prim's Algorithm**
- Grow tree from starting vertex
- Time: O((V + E) log V) with binary heap
- Space: O(V)

### Advanced

**Topological Sort**
- DAG ordering where u before v if u→v
- Kahn: O(V + E)
- DFS: O(V + E)

**Strongly Connected Components (Kosaraju)**
- Time: O(V + E)
- Space: O(V)
- Use: Finding cycles in directed graphs

---

## String Algorithms

**Files**: `algorithms/{python,java}/string_algorithms/`

### Naive Substring Search
- Time: O((n-m+1)*m) = O(n*m)
- Space: O(1)
- Good for short patterns

### KMP (Knuth-Morris-Pratt)
- Failure function preprocessing: O(m)
- Search: O(n + m)
- Space: O(m)
- Advantage: Single pass, no backtracking

### Rabin-Karp
- Rolling hash technique
- Time: O(n + m) average, O(n*m) worst
- Space: O(1)
- Good for multiple pattern matching

---

## Math & Number Theory

**Files**: `algorithms/{python,java}/math_number_theory/`

### GCD (Greatest Common Divisor)
**Euclidean Algorithm**
- Time: O(log(min(a, b)))
- Space: O(1)
- gcd(a, b) = gcd(b, a % b)

### Prime Number Sieve
**Sieve of Eratosthenes**
- Time: O(n log log n)
- Space: O(n)
- Find all primes up to n

### Fast Exponentiation
**Binary Exponentiation**
- Time: O(log n)
- Space: O(1) iterative, O(log n) recursive
- Compute a^b mod m efficiently

---

## Complexity Reference

### Big O Complexity Classes (slowest to fastest)

1. **O(2^n)**: Exponential - avoid if possible
2. **O(n!)**: Factorial - only for small n
3. **O(n³)**: Cubic - okay for n ≤ 500
4. **O(n²)**: Quadratic - okay for n ≤ 10,000
5. **O(n log n)**: Optimal for comparison sorts
6. **O(n)**: Linear - great scaling
7. **O(log n)**: Logarithmic - very fast
8. **O(1)**: Constant - best possible

### What Can Run in Time?

| Time Limit | n = 10^6 | n = 10^5 | n = 10^4 | n = 10^3 | n = 10^2 |
|-----------|----------|----------|----------|----------|----------|
| 1 second | O(n) | O(n) | O(n) | O(n) | O(n²) |
| 1 second | - | O(n log n) | O(n log n) | O(n²) | O(n²) |
| 1 second | - | - | O(n²) | O(n³) | O(2^n) |

---

## Learning Path

### Week 1-2: Fundamentals
- Linear and binary search
- Basic sorting (bubble, insertion, selection)
- Recursion basics

### Week 3-4: Divide & Conquer
- Merge sort, quick sort
- Understanding recurrence relations
- Master theorem

### Week 5-6: Data Structures
- Hash tables for greedy algorithms
- Trees for DP
- Graphs introduction

### Week 7-8: Graph Algorithms
- BFS, DFS, topological sort
- Shortest paths (Dijkstra)
- MST (Kruskal, Prim)

### Week 9-10: Dynamic Programming
- Classic problems (knapsack, LCS, LIS)
- State space and transitions
- Optimization techniques

### Week 11-12: Advanced Topics
- String matching algorithms
- Advanced graph algorithms
- Problem-specific optimizations

