class ListNode:
    """Simple linked list node."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_nodes_with_value(head, val) -> ListNode:
    # Handle case where head nodes need to be deleted
    while head and head.val == val:
        head = head.next

    # If all nodes were deleted
    if not head:
        return None

    # Process the rest of the list
    current = head
    # current.next = current.next.next does not raise AttributeError because:

    # Before this line runs, the loop condition while current.next: ensures that current.next is not None.

    # So current.next.next safely accesses the .next of a valid node (which may be None, but assigning None is valid).
    while current.next:
        if current.next.val == val:
            current.next = current.next.next  # Skip the node with target value
        else:
            current = current.next  # Move to next node only if we didn't delete

    return head


def print_list(head) -> list:
    """Helper function to print the linked list."""
    arr = []
    current = head  # Use a separate pointer to avoid modifying the original list
    while current:
        arr.append(current.val)
        current = current.next
    return arr


# Test the function# Create list: 1 -> 2 -> 2 -> 3 -> 2 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(2)
head.next.next.next.next.next = ListNode(4)

print(f"Original list: {print_list(head)}")

# Delete all nodes with value 2*
head = delete_nodes_with_value(head, 2)
print(f"After deleting 2s: {print_list(head)}")
