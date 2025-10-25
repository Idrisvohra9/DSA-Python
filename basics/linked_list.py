"""
BASIC LINKED LIST IMPLEMENTATION
===============================
A linked list is a linear data structure where elements are stored in nodes.
Each node contains data and a reference (link) to the next node.

Key characteristics:
- Dynamic size (can grow/shrink during runtime)
- Elements not stored in contiguous memory locations
- Efficient insertion/deletion at beginning (O(1))
- Sequential access only (no random access like arrays)

Time Complexities:
- Access: O(n)
- Search: O(n)
- Insertion: O(1) at head, O(n) at specific position
- Deletion: O(1) at head, O(n) at specific position
"""

class ListNode:
    """
    A single node in the linked list.
    Contains data and reference to next node.
    """
    
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The value to store in this node
        """
        self.data = data    # Store the actual data
        self.next = None    # Reference to next node (initially None)


class LinkedList:
    """
    Basic singly linked list implementation.
    Supports common operations like insert, delete, search, etc.
    """
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None    # Reference to first node (initially None)
        self.size = 0       # Keep track of number of elements
    
    def is_empty(self):
        """
        Check if the linked list is empty.
        
        Returns:
            True if list is empty, False otherwise
        """
        return self.head is None
    
    def get_size(self):
        """
        Get the number of elements in the list.
        
        Returns:
            Integer size of the list
        """
        return self.size
    
    def prepend(self, data):
        """
        Insert a new node at the beginning of the list.
        This is the most efficient insertion operation - O(1).
        
        Args:
            data: Value to insert
        """
        # Create a new node with the given data
        new_node = ListNode(data)
        
        # Make new node point to current head
        new_node.next = self.head
        
        # Update head to point to new node
        self.head = new_node
        
        # Increment size counter
        self.size += 1
        
        print(f"Inserted {data} at the beginning")
    
    def append(self, data):
        """
        Insert a new node at the end of the list.
        Requires traversing to the end - O(n).
        
        Args:
            data: Value to insert
        """
        # Create a new node
        new_node = ListNode(data)
        
        # If list is empty, make new node the head
        if self.is_empty():
            self.head = new_node
        else:
            # Traverse to the last node
            current = self.head
            while current.next is not None:
                current = current.next
            
            # Link the last node to new node
            current.next = new_node
        
        # Increment size counter
        self.size += 1
        
        print(f"Inserted {data} at the end")
    
    def insert_at_position(self, data, position):
        """
        Insert a new node at a specific position (0-indexed).
        
        Args:
            data: Value to insert
            position: Index where to insert (0 = beginning)
        """
        # Validate position
        if position < 0 or position > self.size:
            print(f"Invalid position {position}. Valid range: 0 to {self.size}")
            return
        
        # If inserting at beginning, use prepend
        if position == 0:
            self.prepend(data)
            return
        
        # Create new node
        new_node = ListNode(data)
        
        # Traverse to position - 1
        current = self.head
        for i in range(position - 1):
            current = current.next
        
        # Insert new node
        new_node.next = current.next
        current.next = new_node
        
        # Increment size
        self.size += 1
        
        print(f"Inserted {data} at position {position}")
    
    def delete_first(self):
        """
        Delete the first node in the list.
        Most efficient deletion operation - O(1).
        
        Returns:
            Data of deleted node, or None if list is empty
        """
        if self.is_empty():
            print("Cannot delete from empty list")
            return None
        
        # Store data to return
        deleted_data = self.head.data
        
        # Move head to next node
        self.head = self.head.next
        
        # Decrement size
        self.size -= 1
        
        print(f"Deleted {deleted_data} from beginning")
        return deleted_data
    
    def delete_last(self):
        """
        Delete the last node in the list.
        Requires traversing to second-last node - O(n).
        
        Returns:
            Data of deleted node, or None if list is empty
        """
        if self.is_empty():
            print("Cannot delete from empty list")
            return None
        
        # If only one node, delete it
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            print(f"Deleted {deleted_data} from end")
            return deleted_data
        
        # Traverse to second-last node
        current = self.head
        while current.next.next is not None:
            current = current.next
        
        # Store data and remove last node
        deleted_data = current.next.data
        current.next = None
        
        # Decrement size
        self.size -= 1
        
        print(f"Deleted {deleted_data} from end")
        return deleted_data
    
    def delete_by_value(self, value):
        """
        Delete the first occurrence of a specific value.
        
        Args:
            value: Value to delete
        
        Returns:
            True if value was found and deleted, False otherwise
        """
        if self.is_empty():
            print("Cannot delete from empty list")
            return False
        
        # If first node contains the value
        if self.head.data == value:
            self.delete_first()
            return True
        
        # Search for the value in remaining nodes
        current = self.head
        while current.next is not None:
            if current.next.data == value:
                # Found the value, delete it
                current.next = current.next.next
                self.size -= 1
                print(f"Deleted {value} from list")
                return True
            current = current.next
        
        # Value not found
        print(f"Value {value} not found in list")
        return False
    
    def search(self, value):
        """
        Search for a value in the list.
        
        Args:
            value: Value to search for
        
        Returns:
            Index of value if found, -1 otherwise
        """
        current = self.head
        index = 0
        
        while current is not None:
            if current.data == value:
                print(f"Found {value} at index {index}")
                return index
            current = current.next
            index += 1
        
        print(f"Value {value} not found")
        return -1
    
    def get_at_index(self, index):
        """
        Get the value at a specific index.
        
        Args:
            index: Index to access (0-indexed)
        
        Returns:
            Value at index, or None if index is invalid
        """
        if index < 0 or index >= self.size:
            print(f"Invalid index {index}. Valid range: 0 to {self.size - 1}")
            return None
        
        current = self.head
        for i in range(index):
            current = current.next
        
        return current.data
    
    def display(self):
        """
        Display all elements in the list.
        Shows the structure of the linked list.
        """
        if self.is_empty():
            print("List is empty")
            return
        
        elements = []
        current = self.head
        
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print("Linked List: " + " -> ".join(elements) + " -> None")
    
    def reverse(self):
        """
        Reverse the linked list in place.
        Changes the direction of all links.
        """
        if self.is_empty() or self.head.next is None:
            return  # Empty list or single node, nothing to reverse
        
        previous = None
        current = self.head
        
        while current is not None:
            # Store next node
            next_node = current.next
            
            # Reverse the link
            current.next = previous
            
            # Move pointers forward
            previous = current
            current = next_node
        
        # Update head to point to new first node
        self.head = previous
        
        print("List reversed successfully")
    
    def get_middle(self):
        """
        Find the middle element using slow and fast pointer technique.
        
        Returns:
            Data of middle node, or None if list is empty
        """
        if self.is_empty():
            return None
        
        slow = self.head
        fast = self.head
        
        # Move slow one step and fast two steps
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
    
    def detect_cycle(self):
        """
        Detect if there's a cycle in the linked list using Floyd's algorithm.
        
        Returns:
            True if cycle exists, False otherwise
        """
        if self.is_empty():
            return False
        
        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False


# Test the LinkedList implementation
if __name__ == "__main__":
    print("=== BASIC LINKED LIST DEMONSTRATION ===")
    
    # Create a new linked list
    ll = LinkedList()
    
    # Test insertion operations
    print("\n1. Testing insertions:")
    ll.append(10)
    ll.append(20)
    ll.prepend(5)
    ll.insert_at_position(15, 2)
    ll.display()
    print(f"Size: {ll.get_size()}")
    
    # Test search operations
    print("\n2. Testing search:")
    ll.search(15)
    ll.search(100)
    print(f"Element at index 1: {ll.get_at_index(1)}")
    
    # Test deletion operations
    print("\n3. Testing deletions:")
    ll.delete_first()
    ll.display()
    ll.delete_last()
    ll.display()
    ll.delete_by_value(15)
    ll.display()
    
    # Test utility functions
    print("\n4. Testing utility functions:")
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.display()
    print(f"Middle element: {ll.get_middle()}")
    
    # Test reverse
    print("\n5. Testing reverse:")
    ll.reverse()
    ll.display()
    
    # Test edge cases
    print("\n6. Testing edge cases:")
    empty_list = LinkedList()
    empty_list.display()
    empty_list.delete_first()
    empty_list.search(10)