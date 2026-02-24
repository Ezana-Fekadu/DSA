
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
