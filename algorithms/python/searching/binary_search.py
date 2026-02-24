
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
    
    print("\nTest 2: Recursive")
    print(f"Search 7: {binary_search_recursive(arr, 7)}")
    print(f"Search 6: {binary_search_recursive(arr, 6)}")
