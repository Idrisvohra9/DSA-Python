"""
BASIC QUEUE IMPLEMENTATION
=========================
A queue is a linear data structure that follows FIFO (First In, First Out) principle.
Elements are added at the rear (enqueue) and removed from the front (dequeue).

Key characteristics:
- FIFO ordering: first element added is first element removed
- Two main operations: enqueue (add) and dequeue (remove)
- Access only at both ends (front and rear)

Real-world examples:
- People waiting in line
- Print job queue
- CPU task scheduling
- Breadth-first search in graphs

Time Complexities:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Search: O(n)
"""

class QueueNode:
    """
    A single node in the queue.
    Contains data and reference to next node.
    """
    
    def __init__(self, data):
        """
        Initialize a new node.
        
        Args:
            data: The value to store in this node
        """
        self.data = data    # Store the actual data
        self.next = None    # Reference to next node


class Queue:
    """
    Basic queue implementation using linked list.
    Provides efficient O(1) enqueue and dequeue operations.
    """
    
    def __init__(self, max_size=None):
        """
        Initialize an empty queue.
        
        Args:
            max_size: Maximum capacity (None for unlimited)
        """
        self.front = None       # Reference to front node
        self.rear = None        # Reference to rear node
        self.size = 0          # Current number of elements
        self.max_size = max_size  # Maximum capacity
    
    def is_empty(self):
        """
        Check if the queue is empty.
        
        Returns:
            True if queue is empty, False otherwise
        """
        return self.front is None
    
    def is_full(self):
        """
        Check if the queue is full (only relevant if max_size is set).
        
        Returns:
            True if queue is full, False otherwise
        """
        if self.max_size is None:
            return False
        return self.size >= self.max_size
    
    def get_size(self):
        """
        Get the number of elements in the queue.
        
        Returns:
            Integer size of the queue
        """
        return self.size
    
    def enqueue(self, data):
        """
        Add an element to the rear of the queue.
        This is the standard way to add elements to a queue.
        
        Args:
            data: Value to add to the queue
        """
        # Check if queue is full
        if self.is_full():
            print(f"Queue is full! Cannot enqueue {data}")
            return False
        
        # Create a new node
        new_node = QueueNode(data)
        
        # If queue is empty, new node becomes both front and rear
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            # Add new node to rear and update rear pointer
            self.rear.next = new_node
            self.rear = new_node
        
        # Increment size
        self.size += 1
        
        print(f"Enqueued {data}")
        return True
    
    def dequeue(self):
        """
        Remove and return the element from the front of the queue.
        This follows the FIFO principle.
        
        Returns:
            Data of dequeued element, or None if queue is empty
        """
        if self.is_empty():
            print("Queue is empty! Cannot dequeue")
            return None
        
        # Store data to return
        dequeued_data = self.front.data
        
        # Move front pointer to next node
        self.front = self.front.next
        
        # If queue becomes empty, reset rear pointer
        if self.front is None:
            self.rear = None
        
        # Decrement size
        self.size -= 1
        
        print(f"Dequeued {dequeued_data}")
        return dequeued_data
    
    def peek_front(self):
        """
        Look at the front element without removing it.
        
        Returns:
            Data of front element, or None if queue is empty
        """
        if self.is_empty():
            print("Queue is empty!")
            return None
        
        return self.front.data
    
    def peek_rear(self):
        """
        Look at the rear element without removing it.
        
        Returns:
            Data of rear element, or None if queue is empty
        """
        if self.is_empty():
            print("Queue is empty!")
            return None
        
        return self.rear.data
    
    def display(self):
        """
        Display all elements in the queue from front to rear.
        Shows the structure and current state of the queue.
        """
        if self.is_empty():
            print("Queue is empty")
            return
        
        elements = []
        current = self.front
        
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        
        print("Queue (front -> rear): " + " -> ".join(elements))
        print(f"Front: {self.peek_front()}, Rear: {self.peek_rear()}, Size: {self.size}")
    
    def clear(self):
        """
        Remove all elements from the queue.
        """
        self.front = None
        self.rear = None
        self.size = 0
        print("Queue cleared")


class ArrayQueue:
    """
    Queue implementation using a fixed-size array.
    Uses circular array concept to efficiently use space.
    """
    
    def __init__(self, max_size=10):
        """
        Initialize queue with fixed capacity.
        
        Args:
            max_size: Maximum number of elements the queue can hold
        """
        self.max_size = max_size
        self.queue = [None] * max_size  # Fixed-size array
        self.front = 0      # Index of front element
        self.rear = 0       # Index where next element will be added
        self.size = 0       # Current number of elements
    
    def is_empty(self):
        """Check if queue is empty."""
        return self.size == 0
    
    def is_full(self):
        """Check if queue is full."""
        return self.size == self.max_size
    
    def enqueue(self, data):
        """
        Add element to rear of queue using circular array.
        
        Args:
            data: Value to add
        """
        if self.is_full():
            print(f"Queue is full! Cannot enqueue {data}")
            return False
        
        # Add element at rear position
        self.queue[self.rear] = data
        
        # Move rear pointer circularly
        self.rear = (self.rear + 1) % self.max_size
        
        # Increment size
        self.size += 1
        
        print(f"Enqueued {data}")
        return True
    
    def dequeue(self):
        """
        Remove element from front of queue.
        
        Returns:
            Dequeued element or None if empty
        """
        if self.is_empty():
            print("Queue is empty! Cannot dequeue")
            return None
        
        # Get element at front
        dequeued_data = self.queue[self.front]
        
        # Clear the position (optional, for clarity)
        self.queue[self.front] = None
        
        # Move front pointer circularly
        self.front = (self.front + 1) % self.max_size
        
        # Decrement size
        self.size -= 1
        
        print(f"Dequeued {dequeued_data}")
        return dequeued_data
    
    def peek_front(self):
        """Look at front element without removing it."""
        if self.is_empty():
            return None
        return self.queue[self.front]
    
    def display(self):
        """Display current state of the queue."""
        if self.is_empty():
            print("Queue is empty")
            return
        
        elements = []
        index = self.front
        
        for _ in range(self.size):
            elements.append(str(self.queue[index]))
            index = (index + 1) % self.max_size
        
        print("Queue (front -> rear): " + " -> ".join(elements))
        print(f"Front index: {self.front}, Rear index: {self.rear}, Size: {self.size}")


class PriorityQueue:
    """
    Simple priority queue implementation.
    Higher priority values are dequeued first.
    """
    
    def __init__(self):
        """Initialize empty priority queue."""
        self.queue = []  # List of (priority, data) tuples
    
    def enqueue(self, data, priority):
        """
        Add element with given priority.
        
        Args:
            data: Element to add
            priority: Priority value (higher = more important)
        """
        self.queue.append((priority, data))
        # Sort by priority (descending order)
        self.queue.sort(key=lambda x: x[0], reverse=True)
        print(f"Enqueued {data} with priority {priority}")
    
    def dequeue(self):
        """
        Remove and return highest priority element.
        
        Returns:
            Data of highest priority element
        """
        if self.is_empty():
            print("Priority queue is empty!")
            return None
        
        priority, data = self.queue.pop(0)
        print(f"Dequeued {data} (priority {priority})")
        return data
    
    def is_empty(self):
        """Check if priority queue is empty."""
        return len(self.queue) == 0
    
    def display(self):
        """Display all elements with their priorities."""
        if self.is_empty():
            print("Priority queue is empty")
            return
        
        print("Priority Queue (priority, data):")
        for priority, data in self.queue:
            print(f"  ({priority}, {data})")


# Test all queue implementations
if __name__ == "__main__":
    print("=== BASIC QUEUE DEMONSTRATION ===")
    
    # Test 1: Basic Queue (Linked List implementation)
    print("\n1. Testing Basic Queue (Linked List):")
    q = Queue()
    
    # Test enqueue operations
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.display()
    
    # Test dequeue operations
    q.dequeue()
    q.display()
    
    # Test peek operations
    print(f"Front element: {q.peek_front()}")
    print(f"Rear element: {q.peek_rear()}")
    
    # Test 2: Array Queue (Circular Array implementation)
    print("\n2. Testing Array Queue (Circular Array):")
    aq = ArrayQueue(5)
    
    # Fill the queue
    for i in range(5):
        aq.enqueue(i * 10)
    
    aq.display()
    
    # Test circular behavior
    aq.dequeue()
    aq.dequeue()
    aq.enqueue(100)
    aq.enqueue(200)
    aq.display()
    
    # Test 3: Priority Queue
    print("\n3. Testing Priority Queue:")
    pq = PriorityQueue()
    
    # Add elements with different priorities
    pq.enqueue("Low priority task", 1)
    pq.enqueue("High priority task", 5)
    pq.enqueue("Medium priority task", 3)
    pq.enqueue("Critical task", 10)
    
    pq.display()
    
    # Dequeue based on priority
    while not pq.is_empty():
        pq.dequeue()
    
    # Test 4: Bounded Queue
    print("\n4. Testing Bounded Queue:")
    bounded_q = Queue(max_size=3)
    
    # Fill to capacity
    bounded_q.enqueue("A")
    bounded_q.enqueue("B")
    bounded_q.enqueue("C")
    bounded_q.display()
    
    # Try to exceed capacity
    bounded_q.enqueue("D")  # Should fail
    
    # Test 5: Edge Cases
    print("\n5. Testing Edge Cases:")
    empty_q = Queue()
    empty_q.display()
    empty_q.dequeue()  # Dequeue from empty queue
    empty_q.peek_front()  # Peek empty queue
    
    # Single element operations
    single_q = Queue()
    single_q.enqueue("Single")
    single_q.display()
    single_q.dequeue()
    single_q.display()