# Contribution Guide

Thank you for considering contributing to the DSA repository! This guide will help you understand our standards and processes.

## Code Style

### Python

- Follow **PEP 8** style guide
- Use **type hints** for all function parameters and returns
- Use **descriptive names** for variables and functions
- Use **4 spaces** for indentation (never tabs)
- Maximum line length: 100 characters
- Use docstrings for all modules, classes, and public methods

**Example:**

```python
"""Module for binary search implementation."""

from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """Search for target in sorted array.
    
    Args:
        arr: Sorted list of integers
        target: Value to search for
    
    Returns:
        Index of target if found, -1 otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
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
```

### Java

- Follow **Google Java Style Guide**
- Use **Javadoc** for all public classes and methods
- Use **PascalCase** for class names
- Use **camelCase** for method and variable names
- Use **UPPER_SNAKE_CASE** for constants
- Maximum line length: 100 characters
- One public class per file

**Example:**

```java
import java.util.ArrayList;
import java.util.List;

/**
 * Binary Search implementation.
 * 
 * Searches for a target value in a sorted array using binary search.
 */
public class BinarySearch {
    
    /**
     * Searches for the target in a sorted array.
     * 
     * @param arr sorted array of integers
     * @param target value to search for
     * @return index of target if found, -1 otherwise
     * 
     * Time Complexity: O(log n)
     * Space Complexity: O(1)
     */
    public static int search(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return -1;
    }
    
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9};
        System.out.println(search(arr, 5)); // Output: 2
    }
}
```

## File Organization

### Naming Conventions

- **Python files**: `snake_case.py` (e.g., `binary_search_tree.py`)
- **Java files**: `PascalCase.java` (e.g., `BinarySearchTree.java`)
- **Folders**: `snake_case` (e.g., `linked_lists/`, `dynamic_programming/`)

### File Structure

Every implementation file should include:

1. **Module/Class documentation** at the top
   - Description of the data structure/algorithm
   - Key properties or characteristics
   - Time and space complexity for operations

2. **Imports** (organized logically)

3. **Implementation** with clear comments

4. **Demo/Test code** in `if __name__ == "__main__":` (Python) or `main()` method (Java)

## Complexity Documentation

Always document time and space complexity for:

- **Data Structures**: Each core operation (insert, delete, search, etc.)
- **Algorithms**: The overall algorithm and any significant sub-operations

**Format:**

```
Time Complexity: O(n log n) - where n is the size of input
Space Complexity: O(1) - only constant extra space
```

## Testing

Every implementation must include:

1. **Basic test cases** in the main demo section
2. **Edge cases** (empty structures, single element, etc.)
3. **Example usage** showing how to use the implementation

**Python Example:**

```python
if __name__ == "__main__":
    # Test 1: Basic case
    ll = SinglyLinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    print(f"List: {ll}")  # Expected: 1 -> 2 -> 3
    
    # Test 2: Edge case - empty list
    ll2 = SinglyLinkedList()
    print(f"Empty list: {ll2}")  # Expected: empty or None
    
    # Test 3: Delete operation
    ll.delete(2)
    print(f"After delete: {ll}")  # Expected: 1 -> 3
```

## Documentation Requirements

Each subfolder must contain a `README.md` with:

1. **Overview** of the data structures/algorithms in that category
2. **Quick reference table** with complexities
3. **Links** to each implementation
4. **When to use** each structure/algorithm

**Example README.md format:**

```markdown
# Sorting Algorithms

## Overview
This directory contains implementations of common sorting algorithms.

## Quick Reference

| Algorithm | Time (Best) | Time (Avg) | Time (Worst) | Space | Stable |
|-----------|-------------|------------|--------------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |

## Implementations
- [Bubble Sort](bubble_sort.py) - Simple but inefficient
- [Quick Sort](quick_sort.py) - Divide and conquer, average O(n log n)
```

## Pull Request Process

1. **Create a branch** with a descriptive name
   - Example: `feat/add-avl-tree` or `docs/update-readme`

2. **Make your changes** following the style guide

3. **Write clear commit messages**
   - Start with action verb (Add, Fix, Update, etc.)
   - Be specific about what changed
   - Example: "Add AVL tree implementation with comprehensive documentation"

4. **Test thoroughly** before submitting

5. **Submit PR** with:
   - Clear title describing the change
   - Description of what was added/modified
   - Any relevant issue numbers

6. **Address feedback** from reviewers

## Adding New Content

### Adding a New Data Structure

1. Create a subfolder under `data_structures/python/` or `data_structures/java/`
2. Implement in Python following conventions
3. Implement in Java following conventions
4. Create `README.md` in the folder
5. Update main README.md to reference the new structure

### Adding a New Algorithm

1. Create a file in the appropriate `algorithms/{language}/{category}/` folder
2. Implement with full documentation
3. Include complexity analysis
4. Add demo/test code
5. Update the category's README.md

## Common Mistakes to Avoid

- ❌ Not including complexity analysis
- ❌ Missing docstrings/Javadoc
- ❌ Inconsistent naming conventions
- ❌ No example usage or test cases
- ❌ External dependencies without justification
- ❌ Overly complex code without comments
- ❌ Not handling edge cases
- ❌ Incorrect complexity analysis

## Questions or Issues?

If you have questions:

1. Check the main README.md
2. Look at similar implementations
3. Review existing issues/discussions
4. Open a new issue with detailed context

---

Thank you for contributing! 🙏
