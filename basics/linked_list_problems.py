"""
LINKED LIST PROBLEMS & SOLUTIONS
===============================
Collection of well-known linked list problems with optimal solutions.
Each problem includes problem statement, approach, time/space complexity, and implementation.
"""

class ListNode:
    """Standard linked list node definition."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    """Helper function to print linked list."""
    result = []
    current = head
    while current:
        result.append(str(current.val))
        current = current.next
    return " -> ".join(result) + " -> None"

# ============================================================================
# PROBLEM 1: REVERSE LINKED LIST
# ============================================================================
def reverse_list(head):
    """
    Problem: Reverse a singly linked list.
    
    Approach: Use three pointers (previous, current, next) to reverse links.
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Example: 1->2->3->4->5 becomes 5->4->3->2->1
    """
    # Initialize pointers
    previous = None
    current = head
    
    # Traverse and reverse links
    while current:
        # Store next node before breaking the link
        next_node = current.next
        
        # Reverse the link
        current.next = previous
        
        # Move pointers forward
        previous = current
        current = next_node
    
    # Return new head (which was the last node)
    return previous

def reverse_list_recursive(head):
    """
    Recursive solution for reversing linked list.
    Time Complexity: O(n), Space Complexity: O(n) due to recursion stack
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Recursively reverse the rest of the list
    new_head = reverse_list_recursive(head.next)
    
    # Reverse the current connection
    head.next.next = head
    head.next = None
    
    return new_head

# ============================================================================
# PROBLEM 2: DETECT CYCLE IN LINKED LIST
# ============================================================================
def has_cycle(head):
    """
    Problem: Detect if linked list has a cycle.
    
    Approach: Floyd's Cycle Detection Algorithm (Tortoise and Hare)
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Logic: Use two pointers moving at different speeds. If there's a cycle,
    the fast pointer will eventually meet the slow pointer.
    """
    if not head or not head.next:
        return False
    
    # Initialize slow and fast pointers
    slow = head
    fast = head
    
    # Move pointers until they meet or fast reaches end
    while fast and fast.next:
        slow = slow.next        # Move slow pointer one step
        fast = fast.next.next   # Move fast pointer two steps
        
        # If pointers meet, cycle exists
        if slow == fast:
            return True
    
    # Fast pointer reached end, no cycle
    return False

def detect_cycle_start(head):
    """
    Problem: Find the node where cycle begins.
    
    Approach: Two-phase Floyd's algorithm
    1. Detect cycle using slow/fast pointers
    2. Find start by moving one pointer to head and both at same speed
    
    Time Complexity: O(n), Space Complexity: O(1)
    """
    if not head or not head.next:
        return None
    
    # Phase 1: Detect cycle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle found
    
    # Phase 2: Find cycle start
    # Move one pointer to head, keep other at meeting point
    # Move both at same speed until they meet
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow  # This is the start of cycle

# ============================================================================
# PROBLEM 3: MERGE TWO SORTED LINKED LISTS
# ============================================================================
def merge_two_lists(list1, list2):
    """
    Problem: Merge two sorted linked lists into one sorted list.
    
    Approach: Use dummy node and two pointers to compare and merge.
    Time Complexity: O(m + n) where m, n are lengths of lists
    Space Complexity: O(1)
    
    Example: [1,2,4] + [1,3,4] = [1,1,2,3,4,4]
    """
    # Create dummy node to simplify logic
    dummy = ListNode(0)
    current = dummy
    
    # Compare nodes from both lists and add smaller one
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Add remaining nodes from non-empty list
    current.next = list1 or list2
    
    # Return merged list (skip dummy node)
    return dummy.next

# ============================================================================
# PROBLEM 4: FIND MIDDLE OF LINKED LIST
# ============================================================================
def find_middle(head):
    """
    Problem: Find middle node of linked list.
    
    Approach: Two-pointer technique (slow and fast)
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Logic: Slow moves 1 step, fast moves 2 steps. When fast reaches end,
    slow is at middle.
    """
    if not head:
        return None
    
    slow = fast = head
    
    # Move pointers until fast reaches end
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# ============================================================================
# PROBLEM 5: REMOVE NTH NODE FROM END
# ============================================================================
def remove_nth_from_end(head, n):
    """
    Problem: Remove nth node from end of linked list.
    
    Approach: Two-pointer technique with n-gap
    Time Complexity: O(L) where L is length of list
    Space Complexity: O(1)
    
    Logic: Move first pointer n steps ahead, then move both pointers
    until first reaches end. Second pointer will be at nth from end.
    """
    # Use dummy node to handle edge case (removing head)
    dummy = ListNode(0)
    dummy.next = head
    
    first = dummy
    second = dummy
    
    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from end
    second.next = second.next.next
    
    return dummy.next

# ============================================================================
# PROBLEM 6: INTERSECTION OF TWO LINKED LISTS
# ============================================================================
def get_intersection_node(headA, headB):
    """
    Problem: Find intersection node of two linked lists.
    
    Approach: Two-pointer technique with list swapping
    Time Complexity: O(m + n)
    Space Complexity: O(1)
    
    Logic: If lists intersect, pointers will meet at intersection after
    traversing both lists completely.
    """
    if not headA or not headB:
        return None
    
    pointerA = headA
    pointerB = headB
    
    # Continue until pointers meet or both become None
    while pointerA != pointerB:
        # If pointer reaches end, switch to other list's head
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA
    
    return pointerA  # Either intersection node or None

# ============================================================================
# PROBLEM 7: PALINDROME LINKED LIST
# ============================================================================
def is_palindrome(head):
    """
    Problem: Check if linked list is a palindrome.
    
    Approach: 
    1. Find middle using slow/fast pointers
    2. Reverse second half
    3. Compare first and second halves
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return True
    
    # Step 1: Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse second half
    def reverse(node):
        prev = None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev
    
    second_half = reverse(slow)
    
    # Step 3: Compare both halves
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# ============================================================================
# PROBLEM 8: ADD TWO NUMBERS
# ============================================================================
def add_two_numbers(l1, l2):
    """
    Problem: Add two numbers represented as linked lists (digits in reverse order).
    
    Example: (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8)
    Represents: 342 + 465 = 807
    
    Approach: Simulate addition with carry
    Time Complexity: O(max(m, n))
    Space Complexity: O(max(m, n))
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    # Process both lists and carry
    while l1 or l2 or carry:
        # Get values (0 if list is exhausted)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and new carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node with digit
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next nodes
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next

# ============================================================================
# PROBLEM 9: FLATTEN MULTILEVEL DOUBLY LINKED LIST
# ============================================================================
class DoublyListNode:
    """Node for doubly linked list with child pointer."""
    def __init__(self, val=0, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

def flatten_multilevel_list(head):
    """
    Problem: Flatten a multilevel doubly linked list.
    
    Approach: DFS traversal using stack
    Time Complexity: O(n)
    Space Complexity: O(d) where d is maximum depth
    """
    if not head:
        return head
    
    stack = []
    current = head
    
    while current:
        if current.child:
            # If there's a next node, save it for later
            if current.next:
                stack.append(current.next)
            
            # Connect current to child
            current.next = current.child
            current.child.prev = current
            current.child = None
        
        # If no next node and stack has nodes, pop from stack
        if not current.next and stack:
            next_node = stack.pop()
            current.next = next_node
            next_node.prev = current
        
        current = current.next
    
    return head

# ============================================================================
# PROBLEM 10: COPY LIST WITH RANDOM POINTER
# ============================================================================
class RandomListNode:
    """Node with random pointer."""
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

def copy_random_list(head):
    """
    Problem: Deep copy linked list where each node has a random pointer.
    
    Approach: Three-pass algorithm
    1. Create copy nodes interleaved with original
    2. Set random pointers for copy nodes
    3. Separate original and copy lists
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None
    
    # Step 1: Create copy nodes
    current = head
    while current:
        copy_node = RandomListNode(current.val)
        copy_node.next = current.next
        current.next = copy_node
        current = copy_node.next
    
    # Step 2: Set random pointers
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        current = current.next.next
    
    # Step 3: Separate lists
    dummy = RandomListNode(0)
    copy_current = dummy
    current = head
    
    while current:
        copy_current.next = current.next
        current.next = current.next.next
        copy_current = copy_current.next
        current = current.next
    
    return dummy.next

# ============================================================================
# TEST FUNCTIONS
# ============================================================================
def test_linked_list_problems():
    """Test all linked list problems with examples."""
    
    print("=== LINKED LIST PROBLEMS & SOLUTIONS ===\n")
    
    # Test 1: Reverse Linked List
    print("1. REVERSE LINKED LIST")
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(3)
    head1.next.next.next = ListNode(4)
    print(f"Original: {print_list(head1)}")
    reversed_head = reverse_list(head1)
    print(f"Reversed: {print_list(reversed_head)}")
    
    # Test 2: Detect Cycle
    print("\n2. DETECT CYCLE")
    head2 = ListNode(3)
    head2.next = ListNode(2)
    head2.next.next = ListNode(0)
    head2.next.next.next = ListNode(-4)
    head2.next.next.next.next = head2.next  # Create cycle
    print(f"Has cycle: {has_cycle(head2)}")
    
    # Test 3: Merge Two Sorted Lists
    print("\n3. MERGE TWO SORTED LISTS")
    list1 = ListNode(1)
    list1.next = ListNode(2)
    list1.next.next = ListNode(4)
    
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    
    print(f"List 1: {print_list(list1)}")
    print(f"List 2: {print_list(list2)}")
    merged = merge_two_lists(list1, list2)
    print(f"Merged: {print_list(merged)}")
    
    # Test 4: Find Middle
    print("\n4. FIND MIDDLE")
    head4 = ListNode(1)
    head4.next = ListNode(2)
    head4.next.next = ListNode(3)
    head4.next.next.next = ListNode(4)
    head4.next.next.next.next = ListNode(5)
    print(f"List: {print_list(head4)}")
    middle = find_middle(head4)
    print(f"Middle value: {middle.val}")
    
    # Test 5: Check Palindrome
    print("\n5. CHECK PALINDROME")
    head5 = ListNode(1)
    head5.next = ListNode(2)
    head5.next.next = ListNode(2)
    head5.next.next.next = ListNode(1)
    print(f"List: {print_list(head5)}")
    print(f"Is palindrome: {is_palindrome(head5)}")

if __name__ == "__main__":
    test_linked_list_problems()