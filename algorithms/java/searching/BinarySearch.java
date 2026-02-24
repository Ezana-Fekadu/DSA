/**
 * Binary Search Implementation.
 * 
 * Search algorithm for sorted arrays using divide-and-conquer.
 * 
 * Time Complexity: O(log n)
 * Space Complexity: O(1) iterative, O(log n) recursive
 * 
 * Prerequisite: Array must be sorted
 */

public class BinarySearch {
    
    /**
     * Iterative binary search.
     * 
     * @param arr sorted array
     * @param target value to find
     * @return index of target if found, -1 otherwise
     * 
     * Time: O(log n)
     * Space: O(1)
     */
    public static int binarySearchIterative(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;  // Avoid overflow
            
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
    
    /**
     * Recursive binary search.
     * 
     * @param arr sorted array
     * @param target value to find
     * @return index of target if found, -1 otherwise
     * 
     * Time: O(log n)
     * Space: O(log n) for recursion stack
     */
    public static int binarySearchRecursive(int[] arr, int target) {
        return binarySearchRecursiveHelper(arr, target, 0, arr.length - 1);
    }
    
    private static int binarySearchRecursiveHelper(int[] arr, int target, int left, int right) {
        if (left > right) {
            return -1;
        }
        
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            return binarySearchRecursiveHelper(arr, target, mid + 1, right);
        } else {
            return binarySearchRecursiveHelper(arr, target, left, mid - 1);
        }
    }
    
    /**
     * Demo and testing.
     */
    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9, 11, 13, 15};
        
        System.out.println("Test 1: Iterative");
        System.out.println("Search 7: " + binarySearchIterative(arr, 7));
        System.out.println("Search 6: " + binarySearchIterative(arr, 6));
        
        System.out.println("\nTest 2: Recursive");
        System.out.println("Search 7: " + binarySearchRecursive(arr, 7));
        System.out.println("Search 6: " + binarySearchRecursive(arr, 6));
        
        System.out.println("\nTest 3: Edge cases");
        System.out.println("Search first: " + binarySearchIterative(arr, 1));
        System.out.println("Search last: " + binarySearchIterative(arr, 15));
    }
}
