
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
