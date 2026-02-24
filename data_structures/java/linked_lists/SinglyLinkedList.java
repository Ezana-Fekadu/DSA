/**
 * Singly Linked List Implementation.
 * 
 * A linear data structure where each element points to the next.
 * 
 * Operations:
 * - Access: O(n)
 * - Search: O(n)
 * - Insert: O(1) at head, O(n) at tail
 * - Delete: O(1) with pointer, O(n) otherwise
 * 
 * Space Complexity: O(n)
 */

public class SinglyLinkedList<T> {
    
    /**
     * Node class representing each element in the list.
     */
    private static class Node<T> {
        T data;
        Node<T> next;
        
        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }
    
    private Node<T> head;
    
    /**
     * Initialize empty linked list.
     */
    public SinglyLinkedList() {
        this.head = null;
    }
    
    /**
     * Insert element at head.
     * 
     * @param data element to insert
     * Time Complexity: O(1)
     */
    public void insertAtHead(T data) {
        Node<T> newNode = new Node<>(data);
        newNode.next = head;
        head = newNode;
    }
    
    /**
     * Insert element at tail.
     * 
     * @param data element to insert
     * Time Complexity: O(n)
     */
    public void insertAtTail(T data) {
        Node<T> newNode = new Node<>(data);
        if (head == null) {
            head = newNode;
            return;
        }
        
        Node<T> current = head;
        while (current.next != null) {
            current = current.next;
        }
        current.next = newNode;
    }
    
    /**
     * Search for element.
     * 
     * @param data element to find
     * @return true if found, false otherwise
     * Time Complexity: O(n)
     */
    public boolean search(T data) {
        Node<T> current = head;
        while (current != null) {
            if (current.data.equals(data)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }
    
    /**
     * Delete first occurrence of element.
     * 
     * @param data element to delete
     * @return true if deleted, false if not found
     * Time Complexity: O(n)
     */
    public boolean delete(T data) {
        if (head == null) {
            return false;
        }
        
        if (head.data.equals(data)) {
            head = head.next;
            return true;
        }
        
        Node<T> current = head;
        while (current.next != null) {
            if (current.next.data.equals(data)) {
                current.next = current.next.next;
                return true;
            }
            current = current.next;
        }
        return false;
    }
    
    /**
     * String representation.
     */
    @Override
    public String toString() {
        if (head == null) {
            return "Empty";
        }
        
        StringBuilder sb = new StringBuilder();
        Node<T> current = head;
        while (current != null) {
            sb.append(current.data);
            if (current.next != null) {
                sb.append(" -> ");
            }
            current = current.next;
        }
        return sb.toString();
    }
    
    /**
     * Demo and testing.
     */
    public static void main(String[] args) {
        System.out.println("Test 1: Basic operations");
        SinglyLinkedList<Integer> list = new SinglyLinkedList<>();
        list.insertAtTail(1);
        list.insertAtTail(2);
        list.insertAtTail(3);
        System.out.println("List: " + list);
        
        System.out.println("\nTest 2: Insert at head");
        list.insertAtHead(0);
        System.out.println("After insert at head: " + list);
        
        System.out.println("\nTest 3: Search");
        System.out.println("Search 2: " + list.search(2));
        System.out.println("Search 5: " + list.search(5));
        
        System.out.println("\nTest 4: Delete");
        list.delete(2);
        System.out.println("After delete 2: " + list);
    }
}
