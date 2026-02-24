#!/usr/bin/env python3
"""Generate all DSA implementations and READMEs."""

from pathlib import Path

def create_file(path, content):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"Created {path}")

# Binary Search Tree (Python)
bst_python = '''
"""Binary Search Tree Implementation.

Operations:
- Search: O(log n) average, O(n) worst
- Insert: O(log n) average, O(n) worst  
- Delete: O(log n) average, O(n) worst

Space Complexity: O(n)
"""

from typing import Any, Optional


class TreeNode:
    def __init__(self, val: Any):
        self.val = val
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinarySearchTree:
    """BST implementation with insert, search, and delete."""
    
    def __init__(self):
        self.root: Optional[TreeNode] = None
    
    def insert(self, val: Any) -> None:
        """Insert value. Time: O(log n) average."""
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
    
    def _insert_recursive(self, node: TreeNode, val: Any) -> None:
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert_recursive(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert_recursive(node.right, val)
    
    def search(self, val: Any) -> bool:
        """Search for value. Time: O(log n) average."""
        return self._search_recursive(self.root, val)
    
    def _search_recursive(self, node: Optional[TreeNode], val: Any) -> bool:
        if node is None:
            return False
        if node.val == val:
            return True
        elif val < node.val:
            return self._search_recursive(node.left, val)
        else:
            return self._search_recursive(node.right, val)
    
    def inorder(self) -> list:
        """Inorder traversal. Time: O(n)"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[TreeNode], result: list) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.val)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(9)
    
    print(f"Inorder: {bst.inorder()}")
    print(f"Search 3: {bst.search(3)}")
    print(f"Search 6: {bst.search(6)}")
'''

# Binary Search (Python)
binary_search_py = '''
"""Binary Search Implementation.

Time Complexity: O(log n)
Space Complexity: O(1) iterative, O(log n) recursive

Prerequisite: Sorted array
"""

from typing import List


def binary_search_iterative(arr: List[int], target: int) -> int:
    """Iterative binary search.
    
    Returns: Index of target if found, -1 otherwise.
    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: int = None) -> int:
    """Recursive binary search.
    
    Returns: Index of target if found, -1 otherwise.
    Time: O(log n), Space: O(log n)
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    print("Test 1: Iterative")
    print(f"Search 7: {binary_search_iterative(arr, 7)}")
    print(f"Search 6: {binary_search_iterative(arr, 6)}")
    
    print("\\nTest 2: Recursive")
    print(f"Search 7: {binary_search_recursive(arr, 7)}")
    print(f"Search 6: {binary_search_recursive(arr, 6)}")
'''

# Merge Sort (Python)
merge_sort_py = '''
"""Merge Sort Implementation.

Time Complexity: O(n log n) - all cases
Space Complexity: O(n)

Stable sort using divide-and-conquer.
"""

from typing import List


def merge_sort(arr: List[int]) -> List[int]:
    """Sort array using merge sort.
    
    Time: O(n log n), Space: O(n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)


def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted: {sorted_arr}")
'''

# Quick Sort (Python)
quick_sort_py = '''
"""Quick Sort Implementation.

Time Complexity: O(n log n) average, O(n²) worst
Space Complexity: O(log n) for recursion stack

In-place divide-and-conquer sort.
"""

from typing import List


def quick_sort(arr: List[int], low: int = 0, high: int = None) -> None:
    """In-place quick sort.
    
    Time: O(n log n) average, O(n²) worst
    Space: O(log n)
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


def partition(arr: List[int], low: int, high: int) -> int:
    """Partition array around pivot."""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {arr}")
    quick_sort(arr)
    print(f"Sorted: {arr}")
'''

# BFS/DFS (Python)
graph_traversal_py = '''
"""Graph Traversal: BFS and DFS.

Time Complexity: O(V + E) for both
Space Complexity: O(V) for both
"""

from collections import deque, defaultdict
from typing import List, Dict, Set


class Graph:
    """Graph using adjacency list."""
    
    def __init__(self):
        self.graph: Dict[int, List[int]] = defaultdict(list)
    
    def add_edge(self, u: int, v: int) -> None:
        """Add edge (undirected)."""
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def bfs(self, start: int) -> List[int]:
        """Breadth-First Search. Time: O(V + E)"""
        visited: Set[int] = set()
        queue = deque([start])
        visited.add(start)
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node)
            
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    def dfs(self, start: int) -> List[int]:
        """Depth-First Search. Time: O(V + E)"""
        visited: Set[int] = set()
        result = []
        self._dfs_recursive(start, visited, result)
        return result
    
    def _dfs_recursive(self, node: int, visited: Set[int], result: List[int]) -> None:
        visited.add(node)
        result.append(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    
    print(f"BFS from 0: {g.bfs(0)}")
    print(f"DFS from 0: {g.dfs(0)}")
'''

# Create all files
files = {
    "data_structures/python/trees/binary_search_tree.py": bst_python,
    "algorithms/python/searching/binary_search.py": binary_search_py,
    "algorithms/python/sorting/merge_sort.py": merge_sort_py,
    "algorithms/python/sorting/quick_sort.py": quick_sort_py,
    "algorithms/python/graph_algorithms/bfs_dfs.py": graph_traversal_py,
}

for filepath, content in files.items():
    create_file(filepath, content)

print("\nAll implementations created successfully!")
