
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
